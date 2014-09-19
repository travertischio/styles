from django import forms

class BeerForm(forms.Form):
	ibu = forms.IntegerField(label='IBUs', max_value=80)
	srm = forms.IntegerField(label='SRM', max_value=40)
	abv = forms.DecimalField(label='ABV', max_digits=4, decimal_places=2)
	country = forms.CharField(label='Country', max_length=200)