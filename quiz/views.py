# Python import
import random
# django import
from django.db.models import Sum
from django.shortcuts import render
from django.views.generic import TemplateView, View
# local import
from .models import Question, Section


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['object_lst'] = Section.objects.all()
        return context


class QuizApplicationView(View):
    """ Quiz Application Home page """
    template_name = 'quiz/quiz_application.html'
    model = Question

    def get(self, request, slug, *args, **kwargs):
        qs = self.model.objects.query(slug)
        qs_list = list(qs)
        random.shuffle(qs_list)
        total_marks = qs.aggregate(
            total_marks=Sum('number')
        )['total_marks']
        total_quiz = qs.count()
        context = {
            'object_list': qs_list,
            'total_marks': total_marks,
            'total_quiz': total_quiz
        }
        return render(request, self.template_name, context)

    # def post(self, request, *args, **kwargs):
    #     context = self.get_context_data()
    #     qs = self.model.objects.filter(is_active=True)
    #     for obj in qs:
    #         answer = obj.quiz_answer_answer.all()
    #         for ans in answer:
    #             pass
    #     return render(request, self.template_name, context)
