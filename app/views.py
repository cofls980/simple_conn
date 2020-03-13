from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

from .models import Text
from .serializers import TextSerializer
from rest_framework import viewsets

# Create your views here.


class text_restful(viewsets.ModelViewSet):
    queryset = Text.objects.all()
    serializer_class = TextSerializer


@csrf_exempt
def text_insert(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = TextSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(status=400)
    else:
        return JsonResponse(status=400)


@csrf_exempt
def text_delete(request, pk_id):
    if request.method == "POST":
        data = JSONParser().parse(request)
        try:
            td = Text.objects.get(pk=pk_id)
        except (KeyError, Text.DoesNotExist):
            return JsonResponse(status=404)
        serializer = TextSerializer(td, data=data)
        if serializer.is_valid():
            td.delete()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(status=400)
    else:
        return JsonResponse(status=400)


@csrf_exempt
def text_update(request, pk_id):
    if request.method == "POST":
        data = JSONParser().parse(request)
        try:
            td = Text.objects.get(pk=pk_id)
        except (KeyError, Text.DoesNotExist):
            return JsonResponse(status=404)
        serializer = TextSerializer(td, data=data)
        if serializer.is_valid():
            td.txt = data.get("txt")
            td.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(status=400)
    else:
        return JsonResponse(status=400)