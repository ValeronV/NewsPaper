from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'post_type',]

    def clean(self):
        cleaned_data = super().clean()
        author = cleaned_data.get('author')
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")
        post_type = cleaned_data.get('post_type')

        if author is None:
            raise ValidationError({'author': 'Отсутствует автор'})
        elif title is None:
            raise ValidationError({'title': 'Отсутствует заголовок'})
        elif text is None:
            raise ValidationError({'text': 'Отсутствует текст'})
        elif post_type is None:
            raise ValidationError({'post_type': 'Выберите тип поста'})
        return cleaned_data