from django import forms
from django.core.exceptions import ValidationError

from .models import Post, Category, Author


class PostForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.all(), empty_label='Выберете автора', label='Автор')
    title = forms.CharField(max_length = 128, label='Заголовок')
    text = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = ['title', 'text','postCategory','author']

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        title = cleaned_data.get("title")

        if title == text:
            raise ValidationError(
                "Содержание новости не должно быть идентично названию."
            )

        return cleaned_data

