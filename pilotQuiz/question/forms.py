## this is a file that was created for the form entry. It may need to be in
# a different Directory to work.
from django import forms

from .models import Question

class QuestionSelectForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('QuestionReferenceCode',)
