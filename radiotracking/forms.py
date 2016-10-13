from django import forms
from .models import Program, Station

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['title', 'station', 'tz', 'start_time', 'end_time',
                  'mon',
                  'tue',
                  'wed',
                  'thu',
                  'fri',
                  'sat',
                  'sun' ]
        labels = { }

class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = ['name', 'website', 'stream_url', 'band', 'freq', 'location',
            'tz']
        labels = { 'stream_url': 'Streaming URL', 'freq': 'Frequency',
            'tz': 'Time Zone'}
