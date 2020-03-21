# Create your views here.

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
		pk = TrackCountry.objects.filter(country="Pakistan").order_by( "created_at__day", "-created_at",).distinct('created_at__day')
		counter = 0
		growth_factor = {}
		previous_value = None
		for pakistan_record in pk:
			if counter > 0:
				growth_factor["%s - %s" % (previous_value.created_at.strftime("%d %b"),
				                           pakistan_record.created_at.strftime("%d %b"))] = pakistan_record.new_cases / previous_value.new_cases
			counter = counter + 1
			previous_value = pakistan_record
		
		context.update({
			"countries": countries,
			'pakistan_records': pk,
			'growth_factor': growth_factor
		})
		return render(request, self.template_name, context)
