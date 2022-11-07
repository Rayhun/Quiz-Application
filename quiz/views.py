# django import
from django.shortcuts import render
from django.views.generic import TemplateView


class QuizApplicationView(TemplateView):
    """ Quiz Application Home page """
    template_name = 'quiz/quiz_application.html'
