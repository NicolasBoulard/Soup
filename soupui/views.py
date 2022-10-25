from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from soupui.models import OID, Device, Service, Transaction


def index(request):
    template = loader.get_template("index.html")
    context = {"title": "Accueil"}
    if request.user.is_authenticated:
        return HttpResponse(template.render(context, request))
    else:
        return redirect("/login")


def dashboard_device(request, device_id):
    template = loader.get_template("dashboard.html")
    s = Service.objects.get(id=3)
    print(s.transaction_set.all())
    # Transaction.objects.filter(s)

    context = {
        "title": "Dashboard",
        "device_id": device_id,
        "devices": Device.objects.all(),
        "services": Service.objects.filter(device__id=device_id),
    }
    if request.user.is_authenticated:
        return HttpResponse(template.render(context, request))
    else:
        return redirect("/login")


def dashboard(request):
    template = loader.get_template("dashboard.html")
    context = {"title": "Dashboard", "devices": Device.objects.all()}
    if request.user.is_authenticated:
        return HttpResponse(template.render(context, request))
    else:
        return redirect("/login")


def device_remove(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            for checkbox_key in request.POST.keys():
                if checkbox_key != "csrfmiddlewaretoken":
                    Device.objects.get(id=int(checkbox_key)).delete()

        return redirect("/service/device")
    else:
        return redirect("/login")


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
        return redirect("/login")


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
        return redirect("/login")


def device(request):
    template = loader.get_template("device.html")
    context = {"title": "Devices"}
    if request.user.is_authenticated:
        devices = Device.objects.all()
        context["devices"] = devices
        return HttpResponse(template.render(context, request))
    else:
        return redirect("/login")


def oid_remove(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            for checkbox_key in request.POST.keys():
                if checkbox_key != "csrfmiddlewaretoken":
                    OID.objects.get(id=int(checkbox_key)).delete()

        return redirect("/service/OID")
    else:
        return redirect("/login")


def oid_edit(request, oid_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            data = request.POST
            oid = OID.objects.get(id=oid_id)
            oid.name = data["name"]
            oid.identifier = data["identifier"]
            oid.save()

        return redirect("/service/OID")
    else:
        return redirect("/login")


def oid_add(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if "name" or "identifier" in request.POST:
                name = request.POST.get("name")
                identifier = request.POST.get("identifier")
                OID.objects.create(name=name, identifier=identifier)

        return redirect("/service/OID")
    else:
        return redirect("/login")


def oid(request):
    template = loader.get_template("oid.html")
    context = {"title": "OID"}
    if request.user.is_authenticated:
        oids = OID.objects.all()
        context["oids"] = oids
        return HttpResponse(template.render(context, request))
    else:
        return redirect("/login")


def service_remove(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            for checkbox_key in request.POST.keys():
                if checkbox_key != "csrfmiddlewaretoken":
                    Service.objects.get(id=int(checkbox_key)).delete()

        return redirect("/service")
    else:
        return redirect("/login")


def service_edit(request, service_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            data = request.POST
            service = Service.objects.get(id=service_id)
            service.name = data["name"]
            oid_id = data["oid"]
            device_id = data["device"]
            oid = OID.objects.get(id=oid_id)
            device = Device.objects.get(id=device_id)
            service.oid = oid
            service.device = device
            service.save()

        return redirect("/service")
    else:
        return redirect("/login")


def service_add(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if "name" and "device" and "oid" in request.POST:
                name = request.POST.get("name")
                device_id = request.POST.get("device")
                print(device_id)
                oid_id = request.POST.get("oid")
                if device_id != "--------------" and oid_id != "--------------":
                    device = Device.objects.get(id=device_id)
                    oid = OID.objects.get(id=oid_id)
                    Service.objects.create(name=name, device=device, oid=oid)

        return redirect("/service")
    else:
        return redirect("/login")


def service(request):
    template = loader.get_template("service.html")
    context = {"title": "Services"}
    if request.user.is_authenticated:
        services = Service.objects.all()
        oids = OID.objects.all()
        devices = Device.objects.all()
        context["services"] = services
        context["oids"] = oids
        context["devices"] = devices
        return HttpResponse(template.render(context, request))
    else:
        return redirect("/login")


def log(request):
    template = loader.get_template("oid.html")
    context = {"title": "OID"}
    if request.user.is_authenticated:
        oids = OID.objects.all()
        context["oids"] = oids
        return HttpResponse(template.render(context, request))
    else:
        return redirect("/login")
