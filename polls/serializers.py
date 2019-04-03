from rest_framework import serializers
from .models import Phone

class api_exampleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Phone
		fields = '__all__'