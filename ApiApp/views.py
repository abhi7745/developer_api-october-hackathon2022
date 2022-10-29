from django.http import JsonResponse
from django.shortcuts import render

# django restframework
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ApiApp.models import Advocates
from .serializers import AdvocateSerializer
# Create your views here.

@api_view(['get'])
def api(request):
    data = ['welcome/', 'advocates' ,'advocates/username']
    return Response(data)

@api_view(['get'])
def advocate_list(request):
    advocates = Advocates.objects.all()
    serializer = AdvocateSerializer(advocates, many=True)
    return Response(serializer.data)

@api_view(['get'])
def advocate_detail(request, username):
    advocate = Advocates.objects.get(username=username)
    serializer = AdvocateSerializer(advocate, many=False)
    return Response(serializer.data)