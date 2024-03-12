from django.urls import path
from .views import IndexView, RecipeView, RecipeCreateView, RecipeUpdateView, RecipeDeleteView, UserRecipesView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('recipe/<int:pk>', RecipeView.as_view(), name='recipe'),
    path('recipe/create', RecipeCreateView.as_view(), name='recipe_create'),
    path('recipe/<int:pk>/edit', RecipeUpdateView.as_view(), name='recipe_edit'),
    path('recipe/<int:pk>/delete', RecipeDeleteView.as_view(), name='recipe_delete'),
    path('recipe/author/<int:user_id>', UserRecipesView.as_view(), name='user_recipes'),
]
