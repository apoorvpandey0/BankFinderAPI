from rest_framework import serializers

from django.urls import reverse

from ..models import Bank

class BankDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields =["bank_name",'bank_id','district','state','branch','ifsc','city','address']


class BankListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields =["bank_name",'bank_id','district','state','branch','ifsc','city','address']
