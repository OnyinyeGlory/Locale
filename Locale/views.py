from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter

from Locale.models import Region, State, LGA, City
from Locale.serializers import RegionSerializer, StateSerializer, LGASerializer, CitySerializer


class RegionViewSet(ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']
    http_method_names = ['get']


class StateViewSet(ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'capital', 'slogan', 'region__name']
    http_method_names = ['get']


class LGAViewSet(ModelViewSet):
    queryset = LGA.objects.all()
    serializer_class = LGASerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'state__name']
    http_method_names = ['get']


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'state__name']
    http_method_names = ['get']
