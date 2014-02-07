from django.shortcuts import render
from django import forms
from app.forms import ConfigInput
from django.http import HttpResponse

# Create your views here.
def index(request):
    """ EZTLS Homepage"""

    return render(request, 'home.html')

def config_result(request):
    """ EZTLS Generated configuration """

    if request.method == 'POST':
        form = ConfigInput(request.POST)

        if form.is_valid():
            fqdn = form.cleaned_data['fqdn']
            ie6 = form.cleaned_data['ie6']
            win_xp = form.cleaned_data['win_xp']
            force_https = form.cleaned_data['force_https']
            webserver = form.cleaned_data['webservers_choices']
        else:
            form = ConfigInput()
        return render(request, "config_base.html", {'fqdn': fqdn, 'ie6': ie6, 'win_xp': win_xp, 'force_https': force_https, 'webserver': webserver })
    else:
        form = ConfigInput()
        return render(request, 'config_input.html', {'form': form })

