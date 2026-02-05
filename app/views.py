from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Player_Serializer as p
import json
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from .serializers import PlayerSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Create your views here.
def landing(req):
    return render(req,'landing.html')
@csrf_exempt
def seralizeall(req):
    if req.method == "POST":
        print(req.body)
        data =json.loads(req.body)
        serializer = PlayerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    data=p.objects.all()
    seralize=PlayerSerializer(data,many=True)
    print(seralize)
    print(seralize.data)
    j_son=JSONRenderer().render(seralize.data)
    return HttpResponse(j_son,content_type='application/json')
@csrf_exempt
def seralizeone(req,id):
    if req.method == "PUT":
        data = json.loads(req.body)

        obj = p.objects.get(id=id)

        serializer = PlayerSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors)
    if req.method == "PATCH":
        data = json.loads(req.body)
        obj = p.objects.get(id=id)
        serializer = PlayerSerializer(obj, data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    if req.method == "DELETE":
        obj = p.objects.get(id=id)
        obj.delete()
        return JsonResponse({"msg": "deleted"})
    data=p.objects.get(id=id)
    seralize=PlayerSerializer(data)
    return JsonResponse(seralize.data)









    
