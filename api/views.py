from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from api.models import Master, Receiver, Specialization
from api.serializers import MasterSerializer, ReceiverSerializer, SpecializationSerializer
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def master(request, format=None):
    if request.method == 'GET':
        masters = Master.objects.all()
        serializer = MasterSerializer(masters, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MasterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def masterId(request, id, format=None):
    try:
        master = Master.objects.get(id=id)
    except Master.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MasterSerializer(master, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MasterSerializer(master, data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        master.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def masterSpec(request, id, spec):
    try:
        master = Master.objects.get(id=id)
    except master.DoesNotExist:
        return Http404

    master.specs = master.specs + '|' + spec
    serializer = MasterSerializer(master, many=False)
    master.save()
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def masterReceiver(request, id, receiver):
    try:
        master = Master.objects.get(id=id)
    except master.DoesNotExist:
        return Http404

    master.receiver = receiver
    serializer = MasterSerializer(master, many=False)
    master.save()
    return Response(serializer.data)


class ReceiverList(APIView):

    def get(self, request, format=None):
        receivers = Receiver.objects.all()
        serializer = ReceiverSerializer(receivers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReceiverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReceiverDetail(APIView):

    def getReceiver(self, id):
        try:
            receiver = Receiver.objects.get(id=id)
            return receiver
        except receiver.DoesNotExist:
            return Http404

    def get(self, request, id, format=None):
        receiver = self.getReceiver(id)
        serializer = ReceiverSerializer(receiver, many=False)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        receiver = self.getReceiver(id)
        serializer = ReceiverSerializer(receiver, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, id, format=None):
        receiver = self.getReceiver(id)
        serializer = ReceiverSerializer(receiver, many=False)
        receiver.delete()
        return Response(serializer.data)


class SpecializationList(APIView):

    def get(self, request, format=None):
        spec = Specialization.objects.all()
        serializer = SpecializationSerializer(spec, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SpecializationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpecializationDetail(APIView):

    def getSpec(self, id):
        try:
            spec = Specialization.objects.get(id=id)
            return spec
        except spec.DoesNotExist:
            return Http404

    def get(self, request, id, format=None):
        spec = self.getSpec(id)
        serializer = SpecializationSerializer(spec, many=False)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        spec = self.getSpec(id)
        serializer = SpecializationSerializer(spec, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, id, format=None):
        spec = self.getSpec(id)
        serializer = SpecializationSerializer(spec, many=False)
        spec.delete()
        return Response(serializer.data)
