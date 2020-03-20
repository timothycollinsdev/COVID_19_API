# Create your views here.
import json

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import *
from django.views.generic.base import TemplateView

from .serializers import *


class DataView(viewsets.ViewSet):
	
	def list(self, request):
		queryset = CoronaCounrty.objects.all()
		serializer = CoronaCounrtySerializer(queryset, many=True)
		return Response({
			'success': True,
			'result': serializer.data,
		}, status=HTTP_200_OK)


class IndexView(TemplateView):
	template_name = 'index.html'
	
	def get(self, request, *args, **kwargs):
		context = locals()
		countries = CoronaCounrty.objects.all()
		pk = TrackCountry.objects.filter(country="Pakistan").order_by("created_at")
		counter  = 0
		growth_factor = {}
		for pakistan_record in pk.order_by('-created_at__day').distinct('created_at__day'):
			previous_value = pakistan_record
			if counter > 0:
				growth_factor[pakistan_record.created_at.strftime("%Y-%M-%d")] = pakistan_record.new_cases / previous_value.new_cases
			counter = counter + 1
		
		context.update({
			"countries": countries,
			'pakistan_records': pk,
			'growth_factor': growth_factor
		})
		return render(request, self.template_name, context)
