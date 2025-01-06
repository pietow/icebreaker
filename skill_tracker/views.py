from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.db.models import Count
from .models import SkillRating
from .forms import SkillRatingForm
import json

class SkillRatingView(FormView):
    template_name = 'skill_tracker/skill_rating.html'
    form_class = SkillRatingForm
    success_url = reverse_lazy('results')  # Redirect to results page after submission

    def form_valid(self, form):
        # Save the form data to the database
        form.save()
        return super().form_valid(form)


class SkillResultsView(TemplateView):
    template_name = 'skill_tracker/results.html'

    def get_context_data(self, **kwargs):
        # Aggregate counts for each skill level
        context = super().get_context_data(**kwargs)
        context['ratings'] = {
            'linux': list(SkillRating.objects.values('linux').annotate(count=Count('linux'))),
            'python': list(SkillRating.objects.values('python').annotate(count=Count('python'))),
            'database': list(SkillRating.objects.values('database').annotate(count=Count('database'))),
            'git': list(SkillRating.objects.values('git').annotate(count=Count('git'))),
        }
        context['data'] = json.dumps(context['ratings'])  # Convert to JSON for chart
        return context



