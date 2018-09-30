from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class SolvedProblems(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    solved_cc = models.CharField(max_length=10)

class PredictedTags(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    accuracy = models.FloatField()
    tags = models.CharField(max_length=10)



