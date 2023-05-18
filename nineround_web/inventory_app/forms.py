from django.forms import ModelForm, TextInput, DateInput, Textarea
from .models import Event

class EventForm(ModelForm):
    # error_css_class = 'error'
    # required_css_class = 'required'
    class Meta:
        model = Event
        fields = ('nama', 'lokasi', 'tanggal_mulai', 'tanggal_berakhir')
        widgets = {
            'nama' : TextInput(attrs={'class':'eventFormTextField', 'placeholder':'nama event...'}),
            'lokasi': Textarea(attrs={'class':'eventFormTextArea eventFormTextField', 'placeholder':'alamat event...'}),
            'tanggal_mulai': DateInput(
                    format=('%Y-%m-%d'),
                    attrs={'class': 'eventFormTextField', 
                    'placeholder': 'Select a date',
                    'type': 'date'
                    }),
            'tanggal_berakhir': DateInput(
                    format=('%Y-%m-%d'),
                    attrs={'class': 'eventFormTextField', 
                    'placeholder': 'Select a date',
                    'type': 'date'
              }),
        }
    
        