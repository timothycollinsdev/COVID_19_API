from rest_framework import serializers

from .models import *


class CoronaCounrtySerializer(serializers.ModelSerializer):
	class Meta:
		model = CoronaCounrty
		order = ("country", "total_cases",)
		fields = ("country", "total_cases", "new_cases", "total_deaths",
		          "new_deaths", "total_recovered", "active_cases", "serious_cases", "tot_cases")
