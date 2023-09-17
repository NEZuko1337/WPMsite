from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from . import wordlist



def home(request):
    return render(request, 'mainapp/home.html')


def check_word(request):
    input_word = request.GET.get('word')
    exp_words = wordlist.expected_words  # Список ожидаемых слов

    if input_word in exp_words:
        response_data = {'message': 'Слово введено правильно.'}
    else:
        response_data = {'message': 'Введено неправильное слово.'}

    return JsonResponse(response_data)


def words_page(request):
    return render(request, 'mainapp/word.html', {'words': wordlist.expected_words})

