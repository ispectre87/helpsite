from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from helps_app.models import HelpRequest, Region
from .serializers import HelpRequestSerializer, HelpRequestWithSerializer, RegionSerializer
from rest_framework.response import Response
from django.forms import model_to_dict

class HelpRequestsApiView(generics.ListCreateAPIView):
    """Выдает данные с использование сериализатора"""
    queryset = HelpRequest.objects.all()
    serializer_class = HelpRequestSerializer

class HelpRequestsApiViewNoSerializer(APIView):
    """Наследует самый базовый класс. Методы прописывааются"""

    def get(self, request):
        """Обрабатывает get запрос"""
        context = HelpRequest.objects.all().values()
        return Response({'helprequests': list(context)})

    def post(self, request):
        """Обрабатывает post запрос"""
        new_request = Region.objects.create(
            region_name=request.data['region_name']
        )
        return Response(model_to_dict(new_request))

class HelpRequestApiWithSerializer(APIView):
    def get(self, request):
        info = HelpRequest.objects.all()
        return Response(HelpRequestWithSerializer(info, many=True).data)

class RegionApiView(APIView):
    def get(self, request):
        regions = Region.objects.all()
        return Response(RegionSerializer(regions, many=True).data)

    def post(self, request):
        postreq = RegionSerializer(data=request.data)
        postreq.is_valid(raise_exception=True)
        postreq.save()
        return Response(postreq.data)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response("No pk")
        try:
            instance = Region.objects.get(pk=pk)
        except:
            return Response("Doesnot exist")

        upd_region = RegionSerializer(data=request.data, instance=instance)
        upd_region.is_valid(raise_exception=True)
        upd_region.save()

        return Response(upd_region.data)

    def delete(self, response, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response('No pk')


        del_region = Region.objects.filter(pk=pk)
        if not del_region:
            return Response('Record does not exist')

        del_region.delete()
        return Response(f'record {pk} deleted')