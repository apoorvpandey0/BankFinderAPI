import graphene
from graphene_django import DjangoObjectType
from .models import Bank


class BankType(DjangoObjectType):
    class Meta:
        model = Bank
        fields =("id","bank_name",'bank_id','district','state','branch','ifsc','city','address')


class Query(graphene.ObjectType):

    all_banks = graphene.List(BankType)

    def resolve_all_banks(self, info):
        return Bank.objects.all()

schema = graphene.Schema(query=Query)