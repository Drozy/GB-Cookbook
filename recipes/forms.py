from django import forms

from recipes.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'cooking_steps', 'cooking_time', 'tags', 'image', 'author',]
        field_attrs = {'class': 'form-control'}
        widgets = {
            'title': forms.TextInput(attrs=field_attrs),
            'description': forms.Textarea(attrs=field_attrs),
            'ingredients': forms.Textarea(attrs=field_attrs),
            'cooking_steps': forms.Textarea(attrs=field_attrs),
            'tags': forms.CheckboxSelectMultiple(),
        }
