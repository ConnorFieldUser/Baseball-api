# from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from BaseballStats.models import Master, Batting_record, Pitching_record, Fielding_record

from BaseballStats.serializers import MasterSerializer, Batting_recordSerializer, Pitching_recordSerializer, \
                                      Fielding_recordSerializer


# Create your views here.


class MasterListCreateAPIView(ListCreateAPIView):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer


class MasterDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer


class Batting_recordListCreateAPIView(ListCreateAPIView):
    queryset = Batting_record.objects.all()
    serializer_class = Batting_recordSerializer


class Batting_recordDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Batting_record.objects.all()
    serializer_class = Batting_recordSerializer


class Pitching_recordListCreateAPIView(ListCreateAPIView):
    queryset = Pitching_record.objects.all()
    serializer_class = Pitching_recordSerializer


class Pitching_recordDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Pitching_record.objects.all()
    serializer_class = Pitching_recordSerializer


class Fielding_recordListCreateAPIView(ListCreateAPIView):
    queryset = Fielding_record.objects.all()
    serializer_class = Fielding_recordSerializer


class Fielding_recordDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Fielding_record.objects.all()
    serializer_class = Fielding_recordSerializer
