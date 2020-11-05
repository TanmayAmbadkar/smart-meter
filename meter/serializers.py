from rest_framework import serializers
from meter.models import *


class MeterSerializer(serializers.ModelSerializer):

    class Meta:

        model = Meter
        fields = '__all__'


class ReadingSerializer(serializers.ModelSerializer):

    #team = serializers.ReadOnlyField(source='Team')
    class Meta:

        model = Reading
        fields = '__all__'
