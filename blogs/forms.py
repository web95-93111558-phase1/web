from django import forms
from .models import Blog,Post,Comment


class PostForm(forms.Form):
	title = forms.CharField(max_length=200)
	summary = forms.CharField()
	text = forms.CharField()
	



class CommentForm(forms.Form):
	text = forms.CharField()
	
class SearchForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	def clean_text(self):
		text = self.cleaned_data['text']	
		words = len(text.split())
		if words < 2 :
			raise forms.ValidationError("number of words should be more than 2")
		elif words > 10 :
			raise forms.ValidationError("number of words should be less than 10")
		return text