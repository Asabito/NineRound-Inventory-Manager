from django.forms import ModelForm, TextInput, DateInput, Textarea, ChoiceField, NumberInput, Select
from .models import Event, Inventory

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
    
class InventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ('id', 'nama', 'keterangan', 'ukuran', 'harga')
        widgets = {
            'id': TextInput(attrs={'class':'inventoryFormTextfield', 'placeholder':'id item...', 'autofocus':''}),
            'nama': TextInput(attrs={'class':'inventoryFormTextfield', 'placeholder':'nama item...'}),
            'keterangan': TextInput(attrs={'class':'inventoryFormTextfield', 'placeholder':'keterangan item...'}),
            'ukuran': TextInput(attrs={'class':'inventoryFormTextfield', 'placeholder':'ukuran item...'}),
            # 'ukuran': Select(attrs={'class':'inventoryFormTextfield'}),
            'harga': NumberInput(attrs={'class':'inventoryFormTextfield', 'placeholder':'harga item...'}),
        }
    