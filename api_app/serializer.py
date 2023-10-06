from django.db.models import fields
from rest_framework import serializers
from companyapp.models import User,Company

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email')



class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id','company')