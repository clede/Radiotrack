from django import forms
from .models import Program

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['title', 'station', 'start_time', 'end_time',
                  'mon',
                  'tue',
                  'wed',
                  'thu',
                  'fri',
                  'sat',
                  'sun' ]
        labels = { }
