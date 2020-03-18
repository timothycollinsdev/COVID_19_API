from rest_framework import serializers
from .models import *

class CoronaCounrtySerializer(serializers.ModelSerializer):
	class Meta:
		model = CoronaCounrty
		fields = "__all__"
