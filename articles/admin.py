# coding: utf-8
from django.contrib import admin

from articles.models import Article, Tag


# Model możemy zarejestrować z automatycznie utworzonym interfejsem
# Nie podajemy wtedy drugiego argumentu do funkcji `register`
admin.site.register(Tag)


class ArticleAdmin(admin.ModelAdmin):
    fields = ('title', 'content', 'is_visible', 'tags')

# Lub zdefiniować własny tak jak powyżej, a następnie przekazać
# go jako drugi argument do funkcji `register`
admin.site.register(Article, ArticleAdmin)
