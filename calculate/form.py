from .models import Calculation
from django import forms


class CalculationForm(forms.ModelForm):
    class Meta:
        model = Calculation
        fields = ['num_one', 'num_two', 'operator', 'calc_date']
    # calculation_type = forms.IntegerField(widget=forms.Select(
    #   choices=[(0, "+"), (1, "-"), (2, "*"), (3, "/")]))
