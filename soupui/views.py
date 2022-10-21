from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader




def index(request):
    template = loader.get_template("index.html")
    context = {}
    if request.user.is_authenticated:
        return HttpResponse(template.render(context, request))
    else:
        return redirect('/logout')
