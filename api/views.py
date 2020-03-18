# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import *
from .serializers import *

class DataView(viewsets.ViewSet):
	
	def list(self, request):
		queryset = CoronaCounrty.objects.all()
		serializer = CoronaCounrtySerializer(queryset, many=True)
		return Response({
			'success': True,
			'result': serializer.data,
		}, status=HTTP_200_OK)
