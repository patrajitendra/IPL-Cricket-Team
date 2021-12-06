from django.forms import fields
from App.models import*
from django import forms


class AddTeam(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','height':'33px'}))
    icon = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control','height':'33px'}))

    class Meta:
        model=Team
        fields="__all__"
class AddPlayer(forms.ModelForm):
    team=forms.ModelChoiceField(queryset=Team.objects.all(),
                               widget=forms.Select(attrs={'class': 'form-control', 'style': 'height:35px','required':'true','style':'background_color:#F5F8EC'},
                                                   ))
    fullname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','height':'33px'}))
    price=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','height':'33px'}))
    is_playing=forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-control','height':'33px'}))
    role=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','height':'33px'}))
    photo=forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control','height':'33px'}))

    
    class Meta:
        model=Player
        fields="__all__"