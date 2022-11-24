import datetime
import json

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.template import loader

from soupui.models import OID, Device, Service, Transaction, Threshold, Criticality


def logNotificationNumber():
    criticalitys = Criticality.objects.filter(index__lte=4)
    transaction = Transaction.objects.filter(
        service__threshold__criticality__in=criticalitys, viewed=False
    ).distinct()
    return len(transaction)


def index(request):
    template = loader.get_template("index.html")
    context = {"title": "Accueil"}
    log_notif = logNotificationNumber()
    context["log_notif"] = log_notif
    if request.user.is_authenticated:
        return HttpResponse(template.render(context, request))
    else:
        return redirect("/login")


def dashboard_device(request, device_id):
    template = loader.get_template("dashboard_graph.html")

    context = {
        "title": "Dashboard",
        "device_id": device_id,
        "devices": Device.objects.all(),
        "services": Service.objects.filter(device__id=device_id),
    }
    log_notif = logNotificationNumber()
    context["log_notif"] = log_notif
    if request.user.is_authenticated:
        return HttpResponse(template.render(context, request))
    else:
        return redirect("/login")


def dashboard_service(request, device_id, service_id):
    template = loader.get_template("log_service.html")
    service = Service.objects.get(id=service_id)

    context = {
        "title": "Dashboard",
        "device_id": device_id,
        "devices": Device.objects.all(),
        "services": Service.objects.filter(device__id=device_id),
        "service_id": service_id,
        "service": service,
        "transaction_set": service.transaction_set.all().order_by("-date"),
    }
    log_notif = logNotificationNumber()
    context["log_notif"] = log_notif
    if request.user.is_authenticated:
        return HttpResponse(template.render(context, request))
    else:
        return redirect("/login")


def dashboard(request):
    template = loader.get_template("dashboard.html")
    context = {"title": "Dashboard", "devices": Device.objects.all()}
    log_notif = logNotificationNumber()
    context["log_notif"] = log_notif
    if request.user.is_authenticated:
        return HttpResponse(template.render(context, request))
    else:
        return redirect("/login")


def threshold(request):
    template = loader.get_template("threshold.html")
    context = {"title": "Seuil"}
    log_notif = logNotificationNumber()
    context["log_notif"] = log_notif
    if request.user.is_authenticated:
        thresholds = Threshold.objects.all()
        context["thresholds"] = thresholds
        context["criticalitys"] = Criticality.objects.all()
        return HttpResponse(template.render(context, request))
    else:
        return redirect("/login")


def threshold_remove(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            for checkbox_key in request.POST.keys():
                if checkbox_key != "csrfmiddlewaretoken":
                    Threshold.objects.get(id=int(checkbox_key)).delete()

        return redirect("/service/threshold")
    else:
        return redirect("/login")


def threshold_edit(request, threshold_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            if "function" and "value" and "criticality" in request.POST:
                function = request.POST.get("function")
                value = request.POST.get("value")
                criticality_id = request.POST.get("criticality")
                threshold = Threshold.objects.get(id=threshold_id)
                threshold.function = function
                threshold.value = value
                criticality = Criticality.objects.get(id=criticality_id)
                threshold.criticality = criticality
                threshold.save()

        return redirect("/service/threshold")
    else:
        return redirect("/login")


def threshold_add(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if "function" and "value" and "criticality" in request.POST:
                function = request.POST.get("function")
                value = request.POST.get("value")
                criticality = request.POST.get("criticality")
                if (
                    function != "--------------"
                    and criticality != "--------------"
                    and value != ""
                ):
                    criticality = Criticality.objects.get(id=criticality)
                    Threshold.objects.create(
                        function=function, value=value, criticality=criticality
                    )

        return redirect("/service/threshold")
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
    log_notif = logNotificationNumber()
    context["log_notif"] = log_notif
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
    log_notif = logNotificationNumber()
    context["log_notif"] = log_notif
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
                oid_id = request.POST.get("oid")
                thresholds_id = request.POST.get("threshold")
                if (
                    device_id != "--------------"
                    and oid_id != "--------------"
                    and thresholds_id != "--------------"
                ):
                    device = Device.objects.get(id=device_id)
                    oid = OID.objects.get(id=oid_id)
                    print(thresholds_id)
                    thresholds = Threshold.objects.filter(id__in=thresholds_id)
                    service = Service.objects.create(name=name, device=device, oid=oid)
                    service.threshold.set(thresholds)

        return redirect("/service")
    else:
        return redirect("/login")


def service(request):
    template = loader.get_template("service.html")
    context = {"title": "Services"}
    log_notif = logNotificationNumber()
    context["log_notif"] = log_notif
    if request.user.is_authenticated:
        services = Service.objects.all()
        oids = OID.objects.all()
        devices = Device.objects.all()
        thresholds = Threshold.objects.all()
        context["services"] = services
        context["oids"] = oids
        context["devices"] = devices
        context["thresholds"] = thresholds
        return HttpResponse(template.render(context, request))
    else:
        return redirect("/login")


def log(request, view_all):
    template = loader.get_template("log.html")
    context = {"title": "Logs"}
    log_notif = logNotificationNumber()
    context["log_notif"] = log_notif
    if request.user.is_authenticated:
        transaction_signature_list = []
        transaction_list = []
        for transaction in Transaction.objects.all().order_by("-date")[:200][::-1]:
            # TODO fix if no threshold not defined, not transaction showed
            for threshold in transaction.service.threshold.all():
                criticality = threshold.get_criticality_code(transaction)
                if view_all:
                    if not criticality:
                        criticality = Criticality.objects.get(code="INFO")
                        threshold.id = ""
                    transaction_signature = (
                        f"{transaction.id}#{transaction.service.id}#{criticality.code}"
                    )

                    if transaction_signature not in transaction_signature_list:
                        transaction_signature_list.append(transaction_signature)
                        transaction_list.append(
                            {
                                "id": transaction.id,
                                "level": criticality.code,
                                "threshold_id": threshold.id,
                                "service": transaction.service.oid.name,
                                "server": f"{transaction.service.device.ip}:{transaction.service.device.port}",
                                "value": transaction.value,
                                "date": transaction.date.strftime("%m/%d/%Y, %H:%M:%S"),
                                "viewed": transaction.viewed,
                            }
                        )
                else:
                    if criticality:
                        transaction_signature = f"{transaction.id}#{transaction.service.id}#{criticality.code}"

                        if transaction_signature not in transaction_signature_list:
                            transaction_signature_list.append(transaction_signature)
                            transaction_list.append(
                                {
                                    "id": transaction.id,
                                    "level": criticality.code,
                                    "threshold_id": threshold.id,
                                    "service": transaction.service.oid.name,
                                    "server": f"{transaction.service.device.ip}:{transaction.service.device.port}",
                                    "value": transaction.value,
                                    "date": transaction.date.strftime(
                                        "%m/%d/%Y, %H:%M:%S"
                                    ),
                                    "viewed": transaction.viewed,
                                }
                            )
        context["transactions"] = transaction_list
        return HttpResponse(template.render(context, request))
    else:
        return redirect("/login")


def log_detail(request, log_id, threshold_id=""):
    template = loader.get_template("log_detail.html")
    context = {"title": "Log"}
    log_notif = logNotificationNumber()
    context["log_notif"] = log_notif
    if request.user.is_authenticated:
        if not log_id:
            return redirect("/log")
        transaction = Transaction.objects.get(id=log_id)
        if threshold_id:
            threshold = Threshold.objects.get(id=threshold_id)
            criticality = threshold.get_criticality_code(transaction)
            context["threshold"] = threshold
            context["criticality"] = criticality
        context["transaction"] = transaction

        return HttpResponse(template.render(context, request))
    else:
        return redirect("/login")


def transaction_check(request, transaction_id, threshold_id=""):
    if request.user.is_authenticated:
        transaction_id = int(transaction_id)
        transaction = Transaction.objects.get(id=transaction_id)
        if transaction:
            if not transaction.viewed:
                transaction.viewed = True
            else:
                transaction.viewed = False
            transaction.save()
            transactionjson = {}
            transactionjson["transaction"] = transaction.viewed
            if threshold_id:
                return redirect(f"/log/{transaction.id}/{threshold_id}/")
            else:
                return redirect(f"/log/{transaction.id}/")
        else:
            return HttpResponseNotFound("Not found")
    else:
        return redirect("/login")


def transaction_all_check(request):
    if request.user.is_authenticated:
        transaction = Transaction.objects.all().update(viewed=True)
        return redirect("/log/all")
    else:
        return redirect("/login")
