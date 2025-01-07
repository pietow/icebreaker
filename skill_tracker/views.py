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
        context = super().get_context_data(**kwargs)

        # Define all possible levels
        skill_levels = ['beginner', 'intermediate', 'advanced']

        # Helper function to ensure all levels are included
        def fill_missing_levels(data, skill_field):
            # Convert the existing data into a dictionary for easy lookup
            counts = {item[skill_field]: item['count'] for item in data}
            # Ensure all levels are present, add 0 for missing levels
            return [
                {skill_field: level, 'count': counts.get(level, 0)}
                for level in skill_levels
            ]

        # Aggregate and ensure all levels are included
        context['ratings'] = {
            'linux': fill_missing_levels(
                list(SkillRating.objects.values('linux').annotate(count=Count('linux'))),
                'linux'
            ),
            'python': fill_missing_levels(
                list(SkillRating.objects.values('python').annotate(count=Count('python'))),
                'python'
            ),
            'database': fill_missing_levels(
                list(SkillRating.objects.values('database').annotate(count=Count('database'))),
                'database'
            ),
            'git': fill_missing_levels(
                list(SkillRating.objects.values('git').annotate(count=Count('git'))),
                'git'
            ),
        }

        # Convert the result to JSON for the template
        context['data'] = json.dumps(context['ratings'])
        return context

