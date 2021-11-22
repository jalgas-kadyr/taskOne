from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from api.models import Master
from api.serializers import MasterSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# @csrf_exempt
# def masterList(request):
#     if request.method == 'GET':
#         masters = Master.objects.all()
#         serializer = MasterSerializer(masters, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = MasterSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.data, status=400)
#
#
# @csrf_exempt
# def master(request, name):
#     try:
#         master = Master.objects.get(name=name)
#     except Master.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = MasterSerializer(master)
#         return JsonResponse(serializer.data)
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = MasterSerializer(data = data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         master.delete()
#         return HttpResponse(status=204)

@api_view(['GET', 'POST'])
def masters(request):
    if request.method == 'GET':
        masters = Master.objects.all()
        serializer = MasterSerializer(masters, many=True)
        return JsonResponse(serializer.data)
