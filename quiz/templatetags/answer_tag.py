# django import
from django import template
# local import
from quiz.models import Question

register = template.Library()


def question(object):
    qus = Question.objects.get(pk=object)
    print(qus, "*" * 100)
    return qus
