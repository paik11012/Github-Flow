from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    content = forms.CharField(max_length=200)
    score = forms.IntegerField()
    class Meta:
        model = Review
        fields = ['content', 'score', ]