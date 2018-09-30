from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import (
    SolvedProblems,
    PredictedTags
)

User = get_user_model()

@receiver(post_save, sender=User)
def create_profile_handler(sender, instance, created, **kwargs):
    if not created:
        return
    # Create the profile object, only if it is newly created
    solved_problems = SolvedProblems(user=instance)
    predicted_tags = PredictedTags(user=instance)
    
    solved_problems.save()
    predicted_tags.save()
