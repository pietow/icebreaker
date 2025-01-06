from django import forms
from .models import SkillRating

class SkillRatingForm(forms.ModelForm):
    class Meta:
        model = SkillRating
        fields = ['linux', 'python', 'database', 'git']
        widgets = {
            'linux': forms.RadioSelect,
            'python': forms.RadioSelect,
            'database': forms.RadioSelect,
            'git': forms.RadioSelect,
        }

