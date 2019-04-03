from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Question

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']

class AskQuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields= ['question_text', 'pub_date', 'asked_by']
