# django import
from django.contrib import admin
# local import
from.models import Section, Question, Answer


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'is_active']


class AnswerAdmin(admin.StackedInline):
    model = Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'section', 'question', 'number')
    list_filter = ('section__name', )
    search_fields = ('section__name', 'question', 'number')
    inlines = [AnswerAdmin]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer', 'is_correct', 'is_active')
    list_filter = ('question__section__name', )
