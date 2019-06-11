from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

import arrow
from cacheops import cached_as

from .models import Brand, Model, Vehicle, ModelPrice
from .serializers import VehicleSerializer, ModelSerializer

class VehicleView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    filterset_fields = ('model', )
    search_fields = ('traffic_plate_no', 'model__name', 'model__brand__name')

    def get_serializer_class(self):
        if self.action == 'list':
            return VehicleSerializer
        else :
            return VehicleSerializer

    def parent_queryset(self):
        return Vehicle.objects.filter(company__isnull=False).cache()

    def get_queryset(self):
        start_time = self.request.query_params.get('start_time', None)
        end_time = self.request.query_params.get('end_time', None)

        if start_time and end_time: 
            _start_time = arrow.get(start_time).to('Asia/Dubai').strftime('%Y-%m-%d %H:%M:%S')
            _end_time = arrow.get(end_time).to('Asia/Dubai').strftime('%Y-%m-%d %H:%M:%S')
            return self.parent_queryset().filter_job(_start_time, _end_time)

        return self.parent_queryset()

    def list(self, request):
        try:
            response = super().list(request)

            context = {
                'code': 20000,
                'data': response.data,
            }
            
            return Response(context)
        except (ValueError, Exception) as e:
            context = {
                'code': 20001,
                'message': '%s' % e
            }
            return Response(context)

class VehicleModelView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ModelSerializer
    queryset = Model.objects.all().cache()

    def list(self, request):
        try:
            response = super().list(request)

            context = {
                'code': 20000,
                'data': response.data,
            }
            
            return Response(context)
        except (ValueError, Exception) as e:
            context = {
                'code': 20001,
                'message': '%s' % e
            }
            return Response(context)