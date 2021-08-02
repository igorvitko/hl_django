from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    opened = models.BooleanField(default=True)

    def __str__(self):
        return self.question_text
