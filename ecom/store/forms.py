from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    email=forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address' }))
    first_name=forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'first_name'}))
    last_name=forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'last_name'}))
    

    class Meta:
        model=User
        fields=('username', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='User Name'
        self.fields['username'].help_text='<span class="from-text text-muted"><small>Required 150 Characters. Letters, digits and @/./+/-/_ only </small></span>'

        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['placeholder']='Password'
        self.fields['password1'].help_text='<span class="from-text text-muted"><small>Your password cant be too similar to your personal information </small></span>'

        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['placeholder']='Password2'