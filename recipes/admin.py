from django.contrib import admin

from .models import Recipe, Tag


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'author',
        'cooking_time',
        'image',
        'pub_date',
    )
    list_filter = ('tags', 'author',)
    search_fields = ('title', 'author__username')
    autocomplete_fields = ('author',)
    ordering = ('-pub_date',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
