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
    frontDocument = ImageField(upload_to='/photos')
    backDocument = ImageField(upload_to='/photos')
    specs = CharField(max_length=100)

