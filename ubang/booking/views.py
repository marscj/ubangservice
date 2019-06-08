from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ValidationError

from datetime import datetime
import arrow

from .import BookingStatus
from .models import Booking
from .serializers import BookingSerializer, BookingListSerializer, BookingListSimpleSerializer
from .forms import BookingCreateForm

class BookingView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    filterset_fields = ('status', 'create_by')
    search_fields = ('bookingId', 'contact_name', 'contact_phone', 'create_by__name', 'create_by__username', 'vehicle__traffic_plate_no', 'guide__name', 'guide__username',)
    ordering = ('-id',)

    def get_serializer_class(self):
        if self.action == 'list':
            return BookingListSerializer
        else :
            return BookingSerializer

    def parent_queryset(self):
        return Booking.objects.all().filter(company_by=self.request.user.company)

    def get_queryset(self):
        if self.action == 'list':
            queryset = self.parent_queryset()
            start_time = self.request.query_params.get('start_time', None)
            end_time = self.request.query_params.get('end_time', None)

            if start_time and end_time:
                _start_time = arrow.get(start_time).to('Asia/Dubai').strftime('%Y-%m-%d %H:%M:%S')
                _end_time = arrow.get(end_time).to('Asia/Dubai').strftime('%Y-%m-%d %H:%M:%S')
                queryset = queryset.filter(start_time__gte=_start_time).filter(end_time__lte=_end_time)
            return queryset
        else:
            return self.parent_queryset()

    @action(detail=False, methods=['get'])
    def dashboard(self, request):
        queryset = self.parent_queryset().order_by('-id')[:10]

        serializer = BookingListSimpleSerializer(queryset, many=True)

        context = {
            'code': 20000,
            'data': serializer.data,
        }
        
        return Response(context)

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
        serializer = BookingSerializer(data=request.data)

        if not serializer.is_valid():
            if serializer.errors.get('non_field_errors'):
                return Response({
                    'code': 20001,
                    'message': serializer.errors['non_field_errors'][0]
                })
            elif serializer.errors.get('contact_phone'):
                return Response({
                    'code': 20001,
                    'message': serializer.errors['contact_phone'][0]
                })
        try:
            response = super().create(request, *args, **kwargs)
            return Response({
                'code': 20000,
                'data': response.data
            })
        except (ValueError, Exception) as e:
            context = {
                'code': 20001,
                'message': '%s' % e
            }
            return Response(context)