from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from soupui.models import OID, Device


def index(request):
    template = loader.get_template("index.html")
    context = {"title": "Accueil"}
    if request.user.is_authenticated:
        return HttpResponse(template.render(context, request))
    else:
        return redirect("/logout")


def dashboard(request):
    template = loader.get_template("dashboard.html")
    context = {"title": "Dashboard"}
    if request.user.is_authenticated:
        return HttpResponse(template.render(context, request))
    else:
        return redirect("/logout")


def service(request):
    if request.user.is_authenticated:
        return redirect("/service/device")
    else:
        return redirect("/logout")


def device_remove(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            for checkbox_key in request.POST.keys():
                if checkbox_key != "csrfmiddlewaretoken":
                    Device.objects.get(id=int(checkbox_key)).delete()

        return redirect("/service/device")
    else:
        return redirect("/logout")


def device_edit(request, device_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            data = request.POST
            device = Device.objects.get(id=device_id)
            device.name = data["name"]
            device.ip = data["ip"]
            device.port = data["port"]
            device.community = data["community"]
            device.save()

        return redirect("/service/device")
    else:
        return redirect("/logout")


def device_add(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if "name" or "ip" or "port" or "community" in request.POST:
                name = request.POST.get("name")
                ip = request.POST.get("ip")
                port = request.POST.get("port")
                community = request.POST.get("community")
                Device.objects.create(name=name, ip=ip, port=port, community=community)

        return redirect("/service/device")
    else:
        return redirect("/logout")


def device(request):
    template = loader.get_template("device.html")
    context = {"title": "Devices"}
    if request.user.is_authenticated:
        devices = Device.objects.all()
        context["devices"] = devices
        return HttpResponse(template.render(context, request))
    else:
        return redirect("/logout")


def oid(request):
    template = loader.get_template("oid.html")
    context = {"title": "OID"}
    if request.user.is_authenticated:
        oids = OID.objects.all()
        context["oids"] = oids
        return HttpResponse(template.render(context, request))
    else:
        return redirect("/logout")
