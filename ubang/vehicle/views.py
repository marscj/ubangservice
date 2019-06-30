from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

import arrow
from cacheops import cached_as

from .models import Brand, Model, Vehicle, ModelPrice
from .serializers import VehicleSerializer, ModelSerializer

class VehicleView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    filterset_fields = ('model', 'model__category')
    search_fields = ('traffic_plate_no', 'model__name', 'model__brand__name', 'model__category')
    ordering =(
        '-avg_score', '-total_score', 'model__passengers'
    )

    def get_serializer_class(self):
        if self.action == 'list':
            return VehicleSerializer
        else :
            return VehicleSerializer

    def parent_queryset(self):
        return Vehicle.objects.filter(company__isnull=False).filter(is_actived=True).cache()

    def get_queryset(self):
        queryset = self.parent_queryset()
        start_time = self.request.query_params.get('start_time', None)
        end_time = self.request.query_params.get('end_time', None)
        passengers = self.request.query_params.get('passengers', None)

        if start_time is not None and end_time is not None: 
            _start_time = arrow.get(start_time).to('Asia/Dubai').strftime('%Y-%m-%d %H:%M:%S')
            _end_time = arrow.get(end_time).to('Asia/Dubai').strftime('%Y-%m-%d %H:%M:%S')
            queryset =  queryset.filter_job(_start_time, _end_time)

        if passengers is not None:
            queryset = queryset.filter(model__passengers__gte=passengers)

        return queryset

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