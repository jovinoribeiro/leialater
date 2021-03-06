'''
Created on Feb 21, 2015

@author: jovinoribeiro
'''
from django import forms
from django.contrib.auth.models import User

from rango.models import Category, Page, UserProfile


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    view = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    like = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    
    class Meta:
        model = Category
        fields = ('name', 'view', 'like')
        
class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    
    class Meta:
        model = Page
        
        fields = ('title', 'url', 'views')
        
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url
        
        return cleaned_data
    
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, help_text="Please, enter your user name.")
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        fields = ('username', 'password')
           
        
    
    