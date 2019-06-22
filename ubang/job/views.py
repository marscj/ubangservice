from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from django.utils.timezone import now

import arrow

from .serializers import JobSerializer
from .models import Job

class JobViewSet(ModelViewSet):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]
    queryset = Job.objects.all()

    filterset_fields = ('vehicle_id', 'booking_id', 'guide_id')
    ordering = ('-id',)

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