from django import forms
from .models import *
from django.forms.widgets import ClearableFileInput

class MyClearableFileInput(ClearableFileInput):
    initial_text = '현재 사진'
    input_text = '사진 바꾸기'
    clear_checkbox_label = '지우기'

class Boardmodform(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('title', 'information', 'important', 'image', 'cord_sx', 'cord_sy', 'cord_lx', 'cord_ly', 'secure',)
        labels = {
            'title': '제목',
            'information':'내용',
            'important':'중요도',
            'image':'이미지',
            'secure':'공개유무',
            'cord_sx':'',
            'cord_sy':'',
            'cord_lx':'',
            'cord_ly':'',
        }
        error_messages = {
            'secure': {
                'required': "공개유무를 선택해주세요!",
            },
            'important': {
                'required': "영역의 앞뒤 순서를 정해주세요!",
            }
        }
        help_texts = { 'image':'이미지를 추가해 보세요', }
        widgets = {
            'cord_sx':forms.NumberInput(attrs={'style': 'display:none'}),
            'cord_sy':forms.NumberInput(attrs={'style': 'display:none'}),
            'cord_lx':forms.NumberInput(attrs={'style': 'display:none'}),
            'cord_ly':forms.NumberInput(attrs={'style': 'display:none'}),
            'image': MyClearableFileInput(attrs={'style': 'display:block;margin:auto;width:-webkit-fill-available;'}),
            'important':forms.NumberInput(attrs={
                'required':True,
                'placeholder':'영역 앞의 정도',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'제목',
                'style': 'background:#efefef;',
            }),
            'information': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder':'여기를 눌러서 글을 작성할 수 있습니다!\n\n[이용규칙에 어긋나는 행위 금지]\n1. 욕설, 비하, 음란물, 개인정보가 포함된 게시물 게시\n2.특정인이나 단체/지역을 비방하는 행위\n3. 기타 약관 및 현행법에 어긋나는 행위',
                'style': 'background:#efefef;',
            }),
        }
        
class Boardmodform_root(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('title', 'information', 'image', 'secure')
        labels = {
            'title': '제목',
            'information':'내용',
            'image':'이미지',
            'secure':'공개유무',
        }
        help_texts = { 'image':'이미지를 추가해 보세요', }
        widgets = {
            'image': MyClearableFileInput(attrs={'style': 'display:block;margin:auto;width:-webkit-fill-available;'}),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'제목',
                'style': 'background:#efefef;',
            }),
            'information': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder':'여기를 눌러서 글을 작성할 수 있습니다!\n\n[이용규칙에 어긋나는 행위 금지]\n1. 욕설, 비하, 음란물, 개인정보가 포함된 게시물 게시\n2.특정인이나 단체/지역을 비방하는 행위\n3. 기타 약관 및 현행법에 어긋나는 행위',
                'style': 'background:#efefef;',
            }),
        }
        
class CommentTest(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', )
        labels = { 'body': '',}
        widgets = {
            'body': forms.TextInput(attrs={
                'class': 'form-control', 
                'rows':3,
                'id':False,
                'placeholder':'의견작성',
                }),
        }
