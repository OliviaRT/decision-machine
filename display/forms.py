from django.utils.translation import gettext_lazy as _
from django import forms


class DecisionMachineForm(forms.Form):
    """Class to create form that receives data"""

    salary = forms.IntegerField(
        label=_("Salary"), required=True
    )
    expenses = forms.IntegerField(
        label=_("expenses"), required=True
    )
