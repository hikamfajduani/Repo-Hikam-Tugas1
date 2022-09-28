from django import forms

class CreateTodoForm(forms.Form):
    #date = forms.CharField(label="Tanggal")
    title = forms.CharField(label="Judul")
    description = forms.CharField(label="Deskripsi", widget=forms.Textarea)