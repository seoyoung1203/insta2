from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post # 사용할 모델 설정
        fields = ('content', 'image',) # 여기서 사용할 것들