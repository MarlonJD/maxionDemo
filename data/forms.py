from django import forms
from .models import DataSet

class DocumentForm(forms.ModelForm):
    name = forms.CharField(label="Ad Soyad")
    content = forms.ImageField(label="Veri/Fotoğraf")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'label': 'Your name'})
        self.fields['content'].widget.attrs.update({'class': 'form-control-file'})
    class Meta:
        model = DataSet
        fields = ('name', 'content', )