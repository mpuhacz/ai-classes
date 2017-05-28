# coding: utf-8
from django.db import models


class Article(models.Model):

    # Tytuł artykułu
    title = models.CharField(max_length=255)

    # Treść artykułu
    content = models.TextField(null=True, blank=True)

    # Data utworzenia - auto_now_add - jeśli true to ustawia wartość pola jako aktualny
    # czas przy tworzeniu obiektu
    created_at = models.DateTimeField(auto_now_add=True)

    # Tagi przypisane do artykułu
    # Wykorzystujemy tu relacje many-to-many. Jako pierwszy argument podajemy
    # nazwę powiązanego modelu. Koleny argument `related_name` jest opcjonalny.
    # Definiuje on w jaki sposób będziemy odwoływać się do relacji z poziomu instacji
    # modelu Tag. W tym wypadku mając jakąś instację modelu Tag some_tag, odwolalibyśmy się
    # do przypisanych do niego artykułów:
    #     some_tag.articles
    # Bez podania tego argumentu wyglądało by to następująco:
    #     some_tag.article_set
    tags = models.ManyToManyField('Tag', related_name='articles')

    # Czy jest widoczny na stronie? Domyślna wartość - nie.
    is_visible = models.BooleanField(default=False)

    def __str__(self):
        """
        Metoda zwracająca reprezentacje tekstową instancji modelu
        używaną na przykład w panelu administracyjnym.
        """
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
