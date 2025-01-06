from django.urls import path
from .views import SkillRatingView, SkillResultsView

urlpatterns = [
    path('', SkillRatingView.as_view(), name='skill_rating'),
    path('results/', SkillResultsView.as_view(), name='results'),
]

