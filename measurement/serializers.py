from rest_framework import serializers
from .models import Measurement, Sensor


# TODO: опишите необходимые сериализаторы

class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        # fields = ['id', 'name', 'description', 'measurements']
        fields = '__all__'
