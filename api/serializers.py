from rest_framework import serializers
from .models import *


class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = ['name', 'surname', 'patronymic', 'phoneNumber', 'documentNumber', 'issuedBy', 'issuedDate', 'IIN',
                  'status', 'frontDocument', 'backDocument', 'specs']


class ReceiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receiver
        fields = ['name', 'surname', 'patronymic', 'phoneNumber', 'documentNumber', 'issuedBy', 'issuedDate', 'IIN',
                  'status', 'frontDocument', 'backDocument', 'IBAN', 'cardNumber']


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ['name']