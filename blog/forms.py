from django import forms

from .models import Post

# クラスのネスト？
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)