from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published', default=timezone.now)
	asked_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

	def __str__(self):
		return self.question_text

	def get_absolute_url(self):
		return reverse('polls:index')


class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	choice_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

	def __str__(self):
		return self.choice_text

class Phone(models.Model):
	name = models.CharField(max_length= 9000)
	price = models.IntegerField(default=0)
	brand = models.CharField(max_length=200)
	rating = models.IntegerField(default=0)
	specification = models.TextField()

