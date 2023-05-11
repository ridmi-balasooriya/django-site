from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import DataSet


class AddDataForm(forms.ModelForm):
    win = forms.ChoiceField(choices=DataSet.Win_Field,
                            widget=forms.RadioSelect(), initial=0)

    class Meta:
        model = DataSet
        fields = ['date', 'win', 'num_one', 'num_two',
                  'num_three', 'num_four', 'num_five']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'win': forms.RadioSelect,
            'num_one': forms.TextInput(attrs={'placeholder': '1'}),
            'num_two': forms.TextInput(attrs={'placeholder': '2'}),
            'num_three': forms.TextInput(attrs={'placeholder': '3'}),
            'num_four': forms.TextInput(attrs={'placeholder': '4'}),
            'num_five': forms.TextInput(attrs={'placeholder': '5'})
        }


### ------------------ Without Using Models Use Direct Forms  -------------------------- #####
# class AddDataForm(forms.Form):
#     Win_Field = [
#         (1, 'Win'),
#         (0, 'Lose')
#     ]

#     date = forms.DateField(widget=forms.DateInput(
#         attrs={'type': 'date'}), label='')
#     win = forms.ChoiceField(
#         choices=Win_Field, widget=forms.RadioSelect, initial=0)
#     num_one = forms.IntegerField(
#         min_value=1, max_value=49, label='', widget=forms.TextInput(attrs={'placeholder': '1'}))
#     num_two = forms.IntegerField(
#         min_value=1, max_value=49, label='', widget=forms.TextInput(attrs={'placeholder': '2'}))
#     num_three = forms.IntegerField(
#         min_value=1, max_value=49, label='', widget=forms.TextInput(attrs={'placeholder': '3'}))
#     num_four = forms.IntegerField(
#         min_value=1, max_value=49, label='', widget=forms.TextInput(attrs={'placeholder': '4'}))
#     num_five = forms.IntegerField(
#         min_value=1, max_value=49, label='', widget=forms.TextInput(attrs={'placeholder': '5'}))
