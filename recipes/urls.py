from django.urls import path
from .views import IndexView, RecipeView, RecipeCreate

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('recipe/<int:recipe_id>', RecipeView.as_view(), name='recipe'),
    path('recipe/new', RecipeCreate.as_view(), name='recipe_new'),
]
