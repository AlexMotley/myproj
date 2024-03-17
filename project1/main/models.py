from django.db import models


class Word(models.Model):
    word = models.CharField('Слово', max_length=255, unique=True)
    
    def __str__(self):
        return self.word

    class Meta:
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'


class Topic(models.Model):
    topic_title = models.CharField('Тема', max_length=70)
    words = models.ManyToManyField('Word', related_name='topics')
    
    def __str__(self):
        return self.topic_title
    
    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

