from rest_framework import serializers

import arrow

from .models import Job

class JobSerializer(serializers.ModelSerializer):

    start_time = serializers.SerializerMethodField()

    end_time = serializers.SerializerMethodField()
    
    class Meta:
        model = Job
        fields = '__all__'

    def get_start_time(self, obj):
        return arrow.get(obj.start_time).to('Asia/Dubai').strftime('%Y-%m-%d %H:%M')

    def get_end_time(self, obj):
        return arrow.get(obj.start_time).to('Asia/Dubai').strftime('%Y-%m-%d %H:%M')