# Python import
import random
# django import
from django.db.models import Sum
from django.shortcuts import render
from django.views.generic import TemplateView
# local import
from .models import Question, Section


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['object_lst'] = Section.objects.all()
        return context


class QuizApplicationView(TemplateView):
    """ Quiz Application Home page """
    template_name = 'quiz/quiz_application.html'
    model = Question

    def get_context_data(self, **kwargs):
        context = super(QuizApplicationView, self).get_context_data(**kwargs)
        qs = list(self.model.objects.filter(is_active=True))
        random.shuffle(qs)
        context['object_list'] = qs
        context['total_marks'] = self.model.objects.filter(
            is_active=True
        ).aggregate(total_marks=Sum('number'))['total_marks']
        
        context['total_quiz'] = self.model.objects.filter(
            is_active=True
        ).count()
        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        qs = self.model.objects.filter(is_active=True)
        for obj in qs:
            answer = obj.quiz_answer_answer.all()
            for ans in answer:
                pass
        return render(request, self.template_name, context)
