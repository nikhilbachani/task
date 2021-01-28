import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['question_text'], name='unique_question'),
        ]

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=3)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['question', 'choice_text'], name='unique_choice'),
        ]

    def __str__(self):
        return self.choice_text
