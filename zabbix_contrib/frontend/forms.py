from django import forms

from frontend.models import Contribution


class ContributionForm(forms.ModelForm):

    class Meta:
        model = Contribution
