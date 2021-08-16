from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import *


class PollsIndex(ListView):
    model = Question
    template_name = 'hello/index.html'
    context_object_name = 'latest_question_list'
    extra_context = {'title': 'Главная страница'}

    def get_queryset(self):
        return Question.objects.filter(opened=True)


class PollDetail(DetailView):
    model = Question
    template_name = 'hello/detail.html'
    extra_context = {'title': 'Страница опроса'}


class PollResult(DetailView):
    model = Question
    template_name = 'hello/result.html'
    extra_context = {'title': 'Результаты опроса'}


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'hello/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('poll:result', args=(question_id,)))
