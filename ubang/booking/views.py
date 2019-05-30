from django.contrib.admin.options import get_content_type_for_model
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Booking
from .serializers import BookingSerializer, BookingListSerializer

class BookingView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    filterset_fields = ('status', )
    search_fields = ('bookingId', 'contact_name', 'contact_phone', 'create_by__name', 'create_by__username', 'vehicle__traffic_plate_no', 'guide__name', 'guide__username',)

    def get_serializer_class(self):
        if self.action == 'list':
            return BookingListSerializer
        else :
            return BookingSerializer

    def get_queryset(self):
        if self.action == 'list':
            queryset = Booking.objects.all()
            start_time = self.request.query_params.get('start_time', None)
            end_time = self.request.query_params.get('end_time', None)

            print(start_time)
            print(end_time)

            if start_time:
                queryset = queryset.filter(start_time__lte=start_time)
            
            if end_time:
                queryset = queryset.filter(end_time__gte=end_time)

            return queryset
        else:
            return Booking.objects.all()

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

    def retrieve(self, request, pk=None):
        try:
            response = super().retrieve(request, pk)            
            context = {
                'code': 20000,
                'data': response.data
            }
            return Response(context)
        except (ValueError, Exception) as e:  
            context = {
                'code': 20001,
                'message': '%s' % e
            }
            return Response(context)

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            context = {
                'code': 20000,
                'data': response.data
            }
            return Response(context)
        except (ValueError, Exception) as e:
            context = {
                'code': 20001,
                'message': '%s' % e
            }
            return Response(context) 

    def create(self, request, *args, **kwargs):
        print(request.data)
        try:
            response = super().create(request, *args, **kwargs)
            context = {
                'code': 20000,
                'data': response.data
            }
            return Response(context)
        except (ValueError, Exception) as e:
            context = {
                'code': 20001,
                'message': '%s' % e
            }
            return Response(context)