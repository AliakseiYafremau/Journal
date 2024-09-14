from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class CreateLessonForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)


class DeleteLessonForm(forms.Form):
    id = forms.IntegerField()


class CreateCriterionForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), max_length=1000, required=False)
    percent = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0),
        ],
    )
    lesson = forms.CharField(max_length=100)


class DeleteCriterionForm(forms.Form):
    id = forms.IntegerField()


class CreateGradeForm(forms.Form):
    value = forms.FloatField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        validators=[
            MaxValueValidator(10.0),
            MinValueValidator(0.0),
        ]
    )
    criterion = forms.CharField(max_length=100)


class DeleteGradeForm(forms.Form):
    id = forms.IntegerField()