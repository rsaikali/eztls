from django import forms

# Create your models here.
class ConfigInput(forms.Form):
    fqdn = forms.CharField(max_length=50,label='Domain name')
    ie6 = forms.BooleanField(required=False,label='Support IE6')
    win_xp = forms.BooleanField(required=False,label='Support Windows XP')
    force_https = forms.BooleanField(required=False,label='Force https')
    webservers = (('nginx', 'Nginx',), ('apache', 'Apache',))
    webservers_choices = forms.ChoiceField(widget=forms.RadioSelect, choices=webservers, label='Webserver')
