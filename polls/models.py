from django.db import models
from datetime import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=200, default="")
    pub_date = models.DateTimeField(default=datetime.now())


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, default="")
    votes = models.IntegerField(default=0)


