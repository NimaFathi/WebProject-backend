from django.db import models


class search_field(models.Model):
    word = models.CharField(max_length=50)
    post = models.CharField(max_length=50)

    @staticmethod
    def create_search(self, words, post):
        wordss = words.split(' ')
        for word in wordss:
            search_field.create_search(word, post)

    def search(self, word):
        return search_field.objects.filter(word=word)
