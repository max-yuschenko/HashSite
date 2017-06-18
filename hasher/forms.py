from django import forms

from hasher.models import Document

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document', )
