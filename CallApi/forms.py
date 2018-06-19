from django import forms


class RegisterForm(forms.Form):
	first_name = forms.CharField()
	last_name = forms.CharField()
	email = forms.EmailField()
	confirm_email = forms.EmailField()
	password = forms.CharField(max_length=32, widget=forms.PasswordInput)
	confirm_password = forms.CharField(max_length=32, widget=forms.PasswordInput)
	