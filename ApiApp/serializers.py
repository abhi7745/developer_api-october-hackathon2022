from rest_framework.serializers import ModelSerializer
from .models import Advocates, Company


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        # fields = '__all__'
        fields = ['name', 'bio', 'logo']


class AdvocateSerializer(ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = Advocates
        # fields = '__all__'
        fields = ['username', 'name', 'bio', 'profile_pic', 'twitter', 'company']