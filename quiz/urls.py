# from django
from django.urls import path

# local import
from. import views

app_name = 'quiz'

urlpatterns = [
    path('', views.QuizApplicationView.as_view(), name='quiz_application'),
]
