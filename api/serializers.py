from rest_framework import serializers
from .models import *


class MasterSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=30)
    # surname = serializers.CharField(max_length=30)
    # patronymic = serializers.CharField(max_length=30)
    # phoneNumber = serializers.CharField(max_length=12)
    # documentNumber = serializers.CharField(max_length=30)
    # issuedBy = serializers.CharField(max_length=100)
    # issuedDate = serializers.DateField()
    # IIN = serializers.CharField(max_length=12)
    # status = serializers.BooleanField()
    # frontDocument = serializers.ImageField()
    # backDocument = serializers.ImageField()
    # specs = serializers.CharField(max_length =100)
    #
    # def create(self, validated_data):
    #     return Master.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.surname = validated_data.get('surname', instance.surname)
    #     instance.patronymic = validated_data.get('patronymic', instance.patronymic)
    #     instance.phoneNumber = validated_data.get('phoneNumber', instance.phoneNumber)
    #     instance.documentNumber = validated_data.get('documentNumber', instance.documentNumber)
    #     instance.issuedBy = validated_data.get('issuedBy', instance.issuedBy)
    #     instance.issuedDate = validated_data.get('issuedDate', instance.issuedDate)
    #     instance.IIN = validated_data.get('IIN', instance.IIN)
    #     instance.status = validated_data.get('status', instance.status)
    #     instance.frontDocument = validated_data.get('frontDocument', instance.frontDocument)
    #     instance.backDocument = validated_data.get('backDocument', instance.backDocument)
    #     instance.save()
    #     return instance

    class Meta:
        model = Master
        fields = ['name', 'surname', 'patronymic', 'phoneNumber', 'documentNumber', 'issuedBy', 'issuedDate', 'IIN',
                  'status', 'frontDocument', 'backDocument', 'specs']
