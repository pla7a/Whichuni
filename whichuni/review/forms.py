from django import forms
from .models import University, Subject, UniReview

class searchForm(forms.Form):
    university = forms.ModelChoiceField(queryset=University.objects.all())
    subject = forms.ModelChoiceField(queryset=Subject.objects.all())

class submitForm(forms.Form):
    university = forms.ModelChoiceField(queryset=University.objects.all())
    subject = forms.ModelChoiceField(queryset=Subject.objects.all())
    year_started = forms.ChoiceField(UniReview.YEARS)
    current_year = forms.ChoiceField(UniReview.CURRENT)
    review = forms.CharField(widget=forms.Textarea)
    rating = forms.ChoiceField(UniReview.RATING)
    email = forms.EmailField()
