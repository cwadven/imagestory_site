from django import forms
from .models import *

class Categoryform(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('board_name', 'showing_name', 'ordering',)
        labels = { 'board_name': '게시판아이디', 'showing_name':'게시판이름', 'ordering':'게시판순서',}
        #help_texts = { 'title': '필수 사항 입니다!', 'body':'내용을 입력해주세요!'}
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'body': forms.Textarea(attrs={'class': 'form-control',}),
        # }