# coding: utf-8

from django.http.response import Http404
from django.shortcuts import render, get_object_or_404

# from articles.forms import CommentForm
from articles.models import Article


def articles(request):
    # Tworzymy zapytanie które pobierze wszystkie dostępne artykuły
    all_articles = Article.objects.all()

    # Zwracamy obiekt HttpResponse korzystając ze funkcji skrótu render
    # Pierwszy argument to request, kolejny to nazwa templatki
    # trzeci argument to context w którym przekazujemy słownik z danymi
    # które będziemy wykorzysywac w templatce.
    return render(
        request=request,
        template_name='articles.html',
        context={'articles': all_articles}
    )


def article(request, pk):
    # Pobieramy interesujący nas artykuł
    try:
        current_article = Article.objects.get(pk=pk)
    # Jeśli obiekt nie istnieje wyłapujemy wyjątek
    except Article.DoesNotExist:
        # i zwracamy 404
        return Http404()

    return render(request, 'article.html', {'article': current_article})
    # Zobacz również link poniżej. Dla większości przypadków warto skorzystać z podanej tam funkcji.
    # https://docs.djangoproject.com/en/1.11/topics/http/shortcuts/#django.shortcuts.get_object_or_404


# def add_comment(request, article_pk):
#     article = get_object_or_404(Article, pk=article_pk)
#
#     comment_form = CommentForm()
#
#     if request.method == 'POST':
#         # przekaż dane z requesta do formularza
#         comment_form = CommentForm(request.POST)
#         # sprawdź poprawność danych
#         if comment_form.is_valid():
#             comment_form.save()
#
#     return render(request, 'article.html', {'article': article, 'form': comment_form})
