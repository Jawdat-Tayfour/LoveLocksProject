from django import forms 
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta(UserCreationForm):
        model= get_user_model()
        fields = ('username','first_name','last_name','email','age',)

    def save(self, commit=True):
        user = super(CustomUserCreationForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
