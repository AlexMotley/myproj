import os
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from .models import *
from .forms import TopicForm

from django.conf import settings
from django.http import HttpResponse


def index(request):

    if request.method == 'POST' and request.FILES['file_upload']:
        file_obj = request.FILES['file_upload']
        fs = FileSystemStorage()
        file = fs.save(file_obj.name, file_obj)
        words_gathering(file)        

    data = {
        'title': 'Главная страница'
    }
    return render(request, 'main/index.html', data)


def topics_home(request):
    topics = Topic
    # form = TopicForm
    data = {
        'title': 'Темы',
        'topics': topics.objects.all()
        # 'form': form
    }
    return render(request, 'main/topics_home.html', data)


def create(request):
    if request.method == 'POST':
        topic_form = TopicForm(request.POST)
        if topic_form.is_valid():
            selected_words = topic_form.cleaned_data['word']
            new_topic = Topic.objects.create(topic_title=request.POST['topic_name'])
            new_topic.words.add(*selected_words)
            return redirect('topics-home')
    else:
        topic_form = TopicForm()
    data ={
        'title': 'Добавление темы',
        'form': topic_form,
        'words': Word.objects.all()
    }
    return render(request, 'main/create.html', data)
    

def handle_uploaded_file(f):
    with open(f'media/files/{f.name}', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
        words_gathering(f'media/files/{f.name}')


def words_gathering(f):
    # words = set()
    with open(f'{settings.MEDIA_ROOT}\{f}', 'r', encoding='utf-8') as file:
        content = file.read()
        for i_stroke in content.split():
            # words.add(i_stroke)
            word_obj, created = Word.objects.get_or_create(word=i_stroke)
            word_obj.save()
    # for i_word in words:
    #     # try:
    #     word_obj, created = Word.objects.get_or_create(word=i_word)
    #     word_obj.save()
        # except Word.DoesNotExist:
        #     Word.create(word=i_word)

