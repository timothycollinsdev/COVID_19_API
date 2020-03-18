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
		pk = TrackCountry.objects.filter(country="Pakistan")
		context.update({
			"countries": countries,
			'pakistan_records': pk
		})
		return render(request, self.template_name, context)
