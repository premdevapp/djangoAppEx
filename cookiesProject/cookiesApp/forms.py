from  django import forms

class ItemForm(forms.Form):
    name = forms.CharField(max_length=30)
    quantity = forms.IntegerField()