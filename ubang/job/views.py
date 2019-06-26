from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist
from django.utils.timezone import now

import arrow

from .serializers import JobSerializer
from .models import Job
from ubang.booking import BookingStatus

class JobViewSet(ModelViewSet):
    serializer_class = JobSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]
    queryset = Job.objects.all()

    filterset_fields = ('vehicle_id', 'booking_id', 'guide_id', 'day')
    ordering = ('-id',)

    @action(detail=False, methods=['get'])
    def days(self, request):
        query = Job.objects.filter(booking__status=BookingStatus.Created).values('day').annotate(Count=Count('id')).order_by()
        context = {
            'code': 20000,
            'data': query
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
                'message': '%s' % e,
                'data':[]
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
                'message': '%s' % e,
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
            
    @action(detail=True, methods=['get'])
    def checkin(self, request, pk=None):
        checkin_time = arrow.get(now()).to('Asia/Dubai').strftime('%Y-%m-%d %H:%M')

        try:
            job = Job.objects.get(pk=pk)
            job.checkin_time = checkin_time
            job.save()
        except ObjectDoesNotExist:
            return Response({
                'code': 20001,
                'message': 'Not found.'
            })

        return Response({
            'code': 20000,
            'message': 'OK',
            'time': checkin_time
        })
    
    @action(detail=True, methods=['get'])
    def checkout(self, request, pk=None):
        checkout_time = arrow.get(now()).to('Asia/Dubai').strftime('%Y-%m-%d %H:%M')

        try:
            job = Job.objects.get(pk=pk)
            job.checkout_time = checkout_time
            job.save()
        except ObjectDoesNotExist:
            return Response({
                'code': 20001,
                'message': 'Not found.'
            })

        return Response({
            'code': 20000,
            'message': 'OK',
            'time': checkout_time
        })