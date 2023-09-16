from django.http import JsonResponse
from django.shortcuts import render, HttpResponse


def home(request):
    return HttpResponse("<h1>Домашняя страница</h1>")


def check_word(request):
    input_word = request.GET.get('word')
    expected_words = ["Привет", "Пока", "Спасибо"]  # Список ожидаемых слов

    if input_word in expected_words:
        response_data = {'message': 'Слово введено правильно.'}
    else:
        response_data = {'message': 'Введено неправильное слово.'}

    return JsonResponse(response_data)


def words_page(request):
    return render(request, 'mainapp/word.html')

