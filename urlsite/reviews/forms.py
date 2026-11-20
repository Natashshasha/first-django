from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['full_name', 'email', 'text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4}),
        }