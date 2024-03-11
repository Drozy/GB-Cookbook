from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView, FormView, UpdateView, DeleteView

from recipes.forms import RecipeForm
from recipes.models import Recipe


class IndexView(TemplateView):
    template_name = 'recipes/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipes'] = Recipe.objects.order_by('?')[:5]
        return context


class RecipeView(TemplateView):
    template_name = 'recipes/recipe.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = get_object_or_404(Recipe, pk=context['pk'])
        context['recipe'] = recipe
        return context


class RecipeCreate(FormView):
    template_name = 'recipes/recipe_form.html'
    form_class = RecipeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        return redirect(form.save().get_absolute_url())


class RecipeUpdate(UpdateView):
    model = Recipe
    form_class = RecipeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        return redirect(form.save().get_absolute_url())


class RecipeDeleteView(DeleteView):
    model = Recipe
    success_url = reverse_lazy('index')
