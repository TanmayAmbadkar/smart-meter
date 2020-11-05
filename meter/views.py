from django.shortcuts import render
from meter.models import *
from meter.serializers import *
from rest_framework import viewsets
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.response import Response
import requests



class MeterViewSet(viewsets.ModelViewSet):
    queryset = Meter.objects.all()
    serializer_class = MeterSerializer

class ReadingViewSet(viewsets.ModelViewSet):
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer

class AddReading(APIView):

    def post(self, request):
        payload = request.data.get("token") # validate the token
        elements = payload.split('|')
        try:
            meter = Meter.objects.get(device_id = elements[0])
        except:
            return Response({"message": "404 meter does not exist"})

        reading = Reading(meter = meter, current = elements[2], voltage = elements[3], signal_strength = elements[4])
        reading.save()
        response = {}
        response['meter id'] = meter.device_id
        response['reading time'] = reading.clk
        response['reading current'] = reading.current
        response['reading voltage'] = reading.voltage
        response['reading signal'] = reading.signal_strength
        response['message'] = "200 reading registered"
        return Response(response)
