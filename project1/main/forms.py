from .models import Topic, Word
from django.forms import *


class TopicForm(Form):
    # class Meta:
    #      model = Topic
    #      fields = ['title', 'words']

    #      widget = {
    #          'title': TextInput(attrs={
    #              'class': 'form-control',
    #              "placeholder": 'Название темы'
    #          }),
    #      }
    title = TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите название темы'})
    word = ModelMultipleChoiceField(queryset=Word.objects.all(), 
                                    widget=CheckboxSelectMultiple(
                                    # widget=RadioSelect(

        attrs={'class': 'words_choice'}
        ))
