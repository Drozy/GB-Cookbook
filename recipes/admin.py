from django.contrib import admin

from .models import Recipe, Tag, RecipeTag


class RecipeTagsInline(admin.TabularInline):
    model = RecipeTag
    min_num = 1
    extra = 0


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'author',
        'description',
        'cooking_time',
        'image',
        'pub_date',
    )
    inlines = (RecipeTagsInline,)
    list_filter = ('author',)
    search_fields = ('title', 'author__username')
    autocomplete_fields = ('author',)
    ordering = ('-pub_date',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
