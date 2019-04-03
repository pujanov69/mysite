from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Phone
from .serializers import api_exampleSerializer

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.views import generic
from django.views.generic import CreateView

from django.contrib import messages
from .forms import UserRegisterForm, AskQuestionForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime

class PollCreateView(LoginRequiredMixin, CreateView):
	model = Question
	fields = ['question_text']

	def form_valid(self, form):
		form.instance.asked_by = self.request.user
		return super().form_valid(form)

class IndexView(LoginRequiredMixin, generic.ListView):
	login_url = '/login/'
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		return Question.objects.order_by('-pub_date')[:20]


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    login_url = '/login/'

class ResultsView(LoginRequiredMixin, generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    login_url = '/login/'


@login_required
def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {'question': question,'error_message': "You didn't select a choice."})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def first_page(request):
	return render(request, 'polls/first_page.html')


class exampleList(APIView):
	def get(self, request):
		values = Phone.objects.all()
		serializer = api_exampleSerializer(values, many = True)
		return Response(serializer.data)

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You are now able to login')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'polls/register.html', {'form': form})