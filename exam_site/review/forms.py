from django import forms

from exam_site.review.models import Review


class ReviewCreationForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text', 'star_rating']

        widgets = {
            'review_text': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'What do you think about the product?'}),
            'star_rating': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter a number from 1 to 5 to rate the product.'}),
        }
