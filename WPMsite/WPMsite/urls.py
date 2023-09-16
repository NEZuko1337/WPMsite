from django.urls import path
from mainapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('words_page/', views.words_page, name='words_page'),
    path('check_word/', views.check_word, name='check_word')
]