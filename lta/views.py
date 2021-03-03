from django.shortcuts import render
from .models import Students
from django.core import serializers
from django.forms.models import model_to_dict
from django.http import JsonResponse

def index(request):
    users=Students.objects.all()
    return render(request,'crud/crud.html',{'users':users})

def create(request):
    if request.method=='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        obj=Students.objects.create(
            name=name,address=address,phone=phone
        )
        return JsonResponse(model_to_dict(obj),safe=False)

def update(request):
    if request.method=='POST':
        id1=request.POST.get('id')
        name=request.POST.get('name')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
            
        obj=Students.objects.get(pk=id1)
        obj.name=name
        obj.address=address
        obj.phone=phone
        user = {'id':obj.id,'name':obj.name,'address':obj.address,'phone':obj.phone}

        data = {
                'user': user
            }
        return JsonResponse(data)
def delete(request):
    id1 = request.GET.get('id', None)
    Students.objects.get(id=id1).delete()
    data = {
            'deleted': True
        }
    return JsonResponse(data)