from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class sign_up(UserCreationForm):

	class Meta:
		model=User
		fields=('username','password1','password2')

	def __init__(self,*args,**kwargs):
		super(sign_up,self).__init__(*args,**kwargs)

		self.fields['username'].widget.attrs['class']='form-control'
		self.fields['username'].widget.attrs['placeholder']=''
		self.fields['username'].help_text=''
		self.fields['username'].label='USERNAME'


		self.fields['password1'].widget.attrs['class']='form-control'
		self.fields['password1'].widget.attrs['placeholder']=''
		self.fields['password1'].help_text=''
		self.fields['password1'].label='NEW PASSWORD'

		self.fields['password2'].widget.attrs['class']='form-control'
		self.fields['password2'].widget.attrs['placeholder']=''
		self.fields['password2'].help_text=''
		self.fields['password2'].label='RETYPE NEW PASSWORD'