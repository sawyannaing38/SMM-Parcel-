from django.shortcuts import render
from django.http import HttpResponseRedirect 
from django.urls import reverse 
from .helpers import senders, statusList
from .models import Parcel 

from datetime import date

# Create your views here.
def index(request):
    return render(request, "parcel/index.html")

# For Adding Parcel
def choose(request):
    if request.method == "GET":
        return render(request, "parcel/choose.html")
    
    # for post method
    # Getting sender
    senderList = [request.POST.get("sender1"), request.POST.get("sender2"), request.POST.get("sender3")]

    for s in senderList:
        if s:
            sender = s
            break 

    return HttpResponseRedirect(reverse("parcel:add", args=[sender]))

# For adding parcel
def add(request, sender):
    if sender not in senders:
        return HttpResponseRedirect(reverse("parcel:choose"))

    if request.method == "GET":
        return render(request, "parcel/add.html", {
            "sender" : sender,
            "name" : "",
            "phone" : "",
            "item" : "",
            "count" : "",
            "cost" : "",
            "status" : ""
        })
    
    # for get method
    # Getting userinput data
    sender = request.POST.get("sender")
    name = request.POST.get("name")
    phone = request.POST.get("phone")
    item = request.POST.get("item")
    count = request.POST.get("count")
    cost = request.POST.get("cost")
    status = request.POST.get("status")
    action = request.POST.get("action")

    if not sender:
        return render(request,"parcel/add.html", {
            "sender" : sender,
            "name" : name,
            "phone" : phone,
            "item" : item,
            "count" : count,
            "cost" : cost,
            "status" : status,
            "message" : "Missing Sender"
        })
    
    if sender not in senders:
        return render(request,"parcel/add.html", {
            "sender" : sender,
            "name" : name,
            "phone" : phone,
            "item" : item,
            "count" : count,
            "cost" : cost,
            "status" : status,
            "message" : "Invalid Sender"
        })
    
    if not name:
        return render(request,"parcel/add.html", {
            "sender" : sender,
            "name" : name,
            "phone" : phone,
            "item" : item,
            "count" : count,
            "cost" : cost,
            "status" : status,
            "message" : "Missing Name"
        })
    
    if not phone:
        return render(request,"parcel/add.html", {
            "sender" : sender,
            "name" : name,
            "phone" : phone,
            "item" : item,
            "count" : count,
            "cost" : cost,
            "status" : status,
            "message" : "Missing Phone Number"
        })
    
    if not item:
        return render(request,"parcel/add.html", {
            "sender" : sender,
            "name" : name,
            "phone" : phone,
            "item" : item,
            "count" : count,
            "cost" : cost,
            "status" : status,
            "message" : "Missing Item"
        })
    
    if not count:
        return render(request,"parcel/add.html", {
            "sender" : sender,
            "name" : name,
            "phone" : phone,
            "item" : item,
            "count" : count,
            "cost" : cost,
            "status" : status,
            "message" : "Missing Count"
        })
    
    if not cost:
        return render(request,"parcel/add.html", {
            "sender" : sender,
            "name" : name,
            "phone" : phone,
            "item" : item,
            "count" : count,
            "cost" : cost,
            "status" : status,
            "message" : "Missing Cost"
        })
    
    if not status:
        return render(request,"parcel/add.html", {
            "sender" : sender,
            "name" : name,
            "phone" : phone,
            "item" : item,
            "count" : count,
            "cost" : cost,
            "status" : status,
            "message" : "Missing Status"
        })
    
    # Checking valid countinput
    try:
        count = int(count)
    except ValueError:
        return render(request,"parcel/add.html", {
            "sender" : sender,
            "name" : name,
            "phone" : phone,
            "item" : item,
            "count" : count,
            "cost" : cost,
            "status" : status,
            "message" : "Invalid Count Input"
        })
    else:
        if count < 0:
            return render(request,"parcel/add.html", {
            "sender" : sender,
            "name" : name,
            "phone" : phone,
            "item" : item,
            "count" : count,
            "cost" : cost,
            "status" : status,
            "message" : "Invalid Count Input"
        })
    
    # checking valid cost
    try:
        cost = int(cost)
    except ValueError:
        return render(request,"parcel/add.html", {
            "sender" : sender,
            "name" : name,
            "phone" : phone,
            "item" : item,
            "count" : count,
            "cost" : cost,
            "status" : status,
            "message" : "Invalid Cost"
        })
    else:
        if cost < 0:
            return render(request,"parcel/add.html", {
            "sender" : sender,
            "name" : name,
            "phone" : phone,
            "item" : item,
            "count" : count,
            "cost" : cost,
            "status" : status,
            "message" : "Invalid Cost"
        })

    # Checking status input
    if status not in statusList:
        return render(request,"parcel/add.html", {
            "sender" : sender,
            "name" : name,
            "phone" : phone,
            "item" : item,
            "count" : count,
            "cost" : cost,
            "status" : status,
            "message" : "Invalid Status"
        })
    
    # Storing in db
    parcel = Parcel(
        sender = sender,
        name = name,
        phone = phone,
        item = item,
        count = count,
        cost = cost,
        status = status,
        receiveDate = date.today()
    )

    parcel.save()
    
    if action == "add":
        return HttpResponseRedirect(reverse("parcel:add", args=[sender]))
    else:
        return HttpResponseRedirect(reverse("parcel:index"))