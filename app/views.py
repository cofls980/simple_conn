from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.utils import timezone

from .models import Text, Color
from .serializers import TextSerializer, ColorSerializer
from rest_framework import viewsets

# Create your views here.


class text_restful(viewsets.ModelViewSet):
    queryset = Text.objects.all()
    serializer_class = TextSerializer


class color_restful(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


@csrf_exempt
def text_insert(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = TextSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse({"error": "(insert reduplication) Try again!"}, status=201) #400->bad request, 404->not found
    else:
        return JsonResponse(status=400)


@csrf_exempt
def text_delete(request, pk_id):
    if request.method == "POST":
        data = JSONParser().parse(request)
        try:
            td = Text.objects.get(pk=pk_id)
        except (KeyError, Text.DoesNotExist):
            return JsonResponse({"error": "(delete error) Not Exist data"}, status=201)
        txt = td.txt
        if data["txt"] == txt or data["txt"] == "":
            td.delete()
            return JsonResponse({"tid": pk_id, "txt": txt}, status=201)
        else:
            return JsonResponse({"error": "(delete error)Text is not matched."}, status=201)
    else:
        return JsonResponse(status=400)


@csrf_exempt
def text_update(request, pk_id):
    if request.method == "POST":
        data = JSONParser().parse(request)
        try:
            td = Text.objects.get(pk=pk_id)
        except (KeyError, Text.DoesNotExist):
            return JsonResponse({"error": "(update error) Not Exist data"}, status=201)
        txt = td.txt
        serializer = TextSerializer(td, data=data)
        if serializer.is_valid():
            if data["txt"] == txt:
                return JsonResponse({"error": "(update reduplication) Try again!"}, status=201)
            else:
                td.txt = data.get("txt")
                td.save()
                return JsonResponse(serializer.data, status=201)
    else:
        return JsonResponse(status=400)


@csrf_exempt
def color_update(request, pk_id):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ColorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            cd = Color.objects.get(pk=pk_id)
            cd.color = data.get("color")
            cd.save()
            return JsonResponse(serializer.data, status=201)
    else:
        return JsonResponse(status=400)


def color_output(request, pk_id):
    if request.method == "GET":
        co = Color.objects.get(pk=pk_id)
        co.time_access = timezone.now()
        co.save(update_fields=['time_access'])
        return JsonResponse({"color": co.color}, status=201)
    else:
        return JsonResponse(status=400)