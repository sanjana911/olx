from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers


from inventory.models import Vehicle


# Create your views here.

class VehicleListCreateView(APIView):

    def get(self,request):

        instance = Vehicle.objects.all().values()

        response_data = list(instance)

        return Response(response_data)

    def post(self, request):

        form_data = request.data

        running_km = form_data.get("running_km")

        if running_km < 0:

            raise serializers.ValidationError("invalid running_km")

        Vehicle.objects.create(**form_data)

        response_data = {"message":"vehicle created..."}

        return Response(response_data)


class VehicleRetrieveUpdateDeleteView(APIView):

    def get(self,request, pk = None):

        instance = Vehicle.objects.filter(id = pk).values()

        response_data = list(instance)

        return Response(response_data)

    def put(self, request, pk = None):

        form_data = request.data

        Vehicle.objects.filter(id = pk).update(**form_data)

        response_data = {"message":"vehicle updated..."}

        return Response(response_data)

    def delete(self, request, pk = None):

        Vehicle.objects.get(id = pk).delete()

        response_data = {"message":"vehicle is deleted.."}

        return Response(response_data)