from django.db import models

# Create your models here.

class Question(models.Model):
    Quetion_text = models.CharField(max_length=200)
    pub_data = models.DateField("date pusblished")

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)
