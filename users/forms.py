from django import forms
from .models import MyUser

class UserForm(forms.Form):
	user_name = forms.CharField(max_length=100)
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)
	password = forms.CharField(min_length=5)
	email = forms.EmailField()
	
	def clean_user_name(self):
		user_name = self.cleaned_data['user_name']	
		if MyUser.objects.filter(username = user_name).exists():
			raise forms.ValidationError("user name is not valid!")
		return user_name