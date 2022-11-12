# from django
from django.urls import path

# local import
from. import views

app_name = 'quiz'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path(
        'quiz/<str:slug>/', views.QuizApplicationView.as_view(),
        name='quiz_application'
    ),
]
