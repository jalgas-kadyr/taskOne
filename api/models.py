from django.db.models import *


class Master(Model):
    name = CharField(max_length=30)
    surname = CharField(max_length=30)
    patronymic = CharField(max_length=30)
    phoneNumber = CharField(max_length=12)
    documentNumber = CharField(max_length=30)
    issuedBy = CharField(max_length=100)
    issuedDate = DateField()
    IIN = CharField(max_length=12)
    status = BooleanField()
    frontDocument = ImageField(upload_to='photos')
    backDocument = ImageField(upload_to='photos')
    specs = CharField(max_length=100)

    # class Meta():
    #     info = ['name', 'surname', 'patronymic', 'phoneNumber']


class Receiver(Model):
    name = CharField(max_length=30)
    surname = CharField(max_length=30)
    patronymic = CharField(max_length=30)
    phoneNumber = CharField(max_length=12)
    documentNumber = CharField(max_length=30)
    issuedBy = CharField(max_length=100)
    issuedDate = DateField()
    IIN = CharField(max_length=12)
    status = BooleanField()
    frontDocument = ImageField(upload_to='')
    backDocument = ImageField(upload_to='')
    IBAN = CharField(max_length=100)
    cardNumber = CharField(max_length=20)


class Specialization(Model):
    name = CharField(max_length=50)

