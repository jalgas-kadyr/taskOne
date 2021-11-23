from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from api.models import Master
from api.serializers import MasterSerializer
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def masterList(request, format=None):
    masters = Master.objects.all()
    queryset = Master.objects.all()
    serializer = MasterSerializer(masters, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def masterDetail(request, id, format=None):
    try:
        master = Master.objects.get(id=id)
        serializer = MasterSerializer(master, many=False)
        return JsonResponse(serializer.data, safe=False)
    except Exception as error:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def addMaster(request):
    serializer = MasterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes((permissions.AllowAny,))
def changeMaster(request, id, format=None):
    master = Master.objects.get(id=id)
    serializer = MasterSerializer(master, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))
def changeMaster(request, id, format=None):
    master = Master.objects.get(id=id)
    serializer = MasterSerializer(master, data=request.data)
    master.delete()
    return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


