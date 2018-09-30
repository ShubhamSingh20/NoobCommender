from django import forms
'''
from .models import (
    Problem,
    ProgrammerSolution,
)



class TakeCourseForm(forms.ModelForm):
    answer = forms.CharField(
        max_length=100,
        min_length=10,
    )

    class Meta:
        model = ProgrammerSolution
        fields = ('solution',)

    def __init__(self, *args, **kwargs):
        problem = kwargs.pop('problem')
        super().__init__(*args, **kwargs)
        self.fields['solution'].queryset = problem.solution.order_by('text')
'''