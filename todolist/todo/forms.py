from django import forms

from django.contrib.admin.widgets import AdminDateWidget

from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'author', 'category', 'deadline', ]

        #ウィジェットはフォームとかの部品の種類を指定する要素
        #djangoのフォームウィジェットにHTML属性を付与する(attrs)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),  # カテゴリが選択肢の場合
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),

        }


