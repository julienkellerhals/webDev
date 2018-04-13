from django import forms

class signupForm(forms.Form):
	user_name = forms.CharField(label='username', max_length=25)
	name = forms.CharField(label='name', max_length=25)
	last_name = forms.CharField(label='lastname', max_length=25)
	email = forms.EmailField(label='email')
	password = forms.CharField(label='password', max_length=25)
	projects = forms.CharField(label='Projects') # TODO
	status = forms.MultipleChoiceField(label='status')
	profile_pic = forms.CharField(label='pic', max_length=30) # path 
