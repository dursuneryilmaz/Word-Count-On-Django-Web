from django import forms
from .models import WordCount


class WordCountForm(forms.ModelForm):
    #title = forms.CharField(max_length=200)
    #app_name = forms.CharField(max_length=200)
    #file = forms.FileField()

    class Meta:
        model = WordCount
        fields = [
            'title',
            'app_name',
            'comments',
            'file'

        ]
