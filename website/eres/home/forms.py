from django import forms

from . models import Usuario

class ContactForm(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'

    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
            super(ContactForm, self).__init__(*args, **kwargs)
            self.fields['contact_name'].label = "Your name:"
            self.fields['contact_email'].label = "Your email:"
            self.fields['content'].label = "What do you want to say?"


#class UserForm(forms.Form):
#    class Meta:
#        model = Usuario

#    username = forms.CharField(required=True)
#    password = forms.CharField(required=True, widget=forms.PasswordInput)
#    def __init__(self, *args, **kwargs):
#            super(UserForm, self).__init__(*args, **kwargs)
#            self.fields['username'].label = "Username:"
#            self.fields['password'].label = "Password:"
