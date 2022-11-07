# django import
from django.contrib import admin
# local import
from.models import *


@admin.site.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'is_active']


@admin.site.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'section', 'question', 'number')


@admin.site.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer', 'is_correct', 'is_active')
