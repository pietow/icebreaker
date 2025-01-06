from django.db import models

from django.db import models

class SkillRating(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    linux = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    python = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    database = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    git = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

