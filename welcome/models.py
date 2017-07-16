from __future__ import unicode_literals
from django.db import models


from django.contrib.auth.models import User

from django.utils import timezone
import datetime
# Create your models here.

'''class Question(models.Model):
    question_text = models.CharField('Question ',max_length=500,help_text="Enter your Question")
    pub_date = models.DateTimeField(help_text='Date Published',auto_now_add=True,blank=True)
    def __str__(self):
        return self.question_text
    
'''




class Question(models.Model):
        question = models.TextField(max_length=200, default="")
        option1 = models.CharField(max_length=50, default="")
        option2 = models.CharField(max_length=50, default="")
        option3 = models.CharField(max_length=50, default="")
        option4 = models.CharField(max_length=50, default="")
        answer = models.CharField(max_length=50, default="")
        def __str__(self):
            return self.question

'''class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True)
    choice_text = models.CharField('Poll Option',max_length=200,help_text="Enter Poll option for Choosen Question")
    votes = models.IntegerField(default=0,help_text="Enter Vote Count")
    def __str__(self):
        return self.choice_text
'''
