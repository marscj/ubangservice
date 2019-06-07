from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework.mixins import ListModelMixin
from rest_framework import generics
from rest_framework import filters

import arrow

from .serializers import UserSerializer, PermissionSerializer, RoleSerializer
from .models import CustomUser, Permission, Role

class LoginJwtTokenView(ObtainJSONWebToken):
    
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        
        if response.status_code == 200:
            context = {
                'code': 20000,
                'data': response.data,
            }
        else:
            context = {
                'code': 20001,
                'message': 'Unable to log in with provided credentials.'
            }
        
        return Response(context)

class LogoutJwtTokenView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        context = {
            'code': 20000,
            'message': 'ok'
        }
        return Response(context)

class UserView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    
    filterset_fields = ('is_driver', 'is_tourguide', 'is_actived', 'company')
    search_fields = ('username', 'email')

    def parent_queryset(self):
        return CustomUser.objects.filter(company__isnull=False)

    def get_queryset(self):
        start_time = self.request.query_params.get('start_time', None)
        end_time = self.request.query_params.get('end_time', None)

        if start_time and end_time: 
            _start_time = arrow.get(start_time).to('Asia/Dubai').strftime('%Y-%m-%d %H:%M:%S')
            _end_time = arrow.get(end_time).to('Asia/Dubai').strftime('%Y-%m-%d %H:%M:%S')
            return CustomUser.objects.filter_job(_start_time, _end_time)

        return self.parent_queryset()

    def list(self, request):
        response = super().list(request)
        
        context = {
            'code': 20000,
            'data': response.data,
        }

        return Response(context)

    @action(detail=False, methods=['get'])
    def info(self, request):
        serializer = UserSerializer(request.user)
        context = {
            'code': 20000,
            'data': serializer.data
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

class RoleView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = RoleSerializer
    queryset = Role.objects.all()
    
    filterset_fields = ('company',)
    
    def get_queryset(self):
        return Role.objects.all()

    def list(self, request):
        response = super().list(request)
        
        context = {
            'code': 20000,
            'data': response.data,
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
            print(e)
            return Response(context)

    def destroy(self, request, *args, **kwargs):
        try:
            response = super().destroy(request, *args, **kwargs)
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

class PermissionView(generics.ListAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        
        context = {
            'code': 20000,
            'data': response.data,
        }

        return Response(context)