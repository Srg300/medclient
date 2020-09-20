from django import forms

class Drug(forms.Form):
    title =  forms.CharField(label= 'drug_title', max_length=100)
    dose = forms.CharField(label ='drug_dose',max_length=20, empty_value='не указанно' )
