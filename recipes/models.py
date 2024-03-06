from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class Recipe(models.Model):
    title = models.CharField('Название рецепта', max_length=200)
    description = models.TextField('Описание рецепта')
    ingredients = models.TextField('Ингридиенты')
    cooking_steps = models.TextField('Шаги приготовления')
    cooking_time = models.PositiveSmallIntegerField('Время приготовления')
    image = models.ImageField('Изображение', upload_to='recipes/')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes', verbose_name='Автор рецепта')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'рецепт'
        verbose_name_plural = 'рецепты'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipe', kwargs={'recipe_id': self.pk})


class Tag(models.Model):
    title = models.CharField('Категория', max_length=50, db_index=True)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.title


class RecipeTag(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='tags', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, related_name='recipes', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
