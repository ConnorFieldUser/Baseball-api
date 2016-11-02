
from rest_framework import serializers

from BaseballStats.models import Master, Batting_record, Pitching_record, Fielding_record


class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = '__all__'


class Batting_recordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batting_record
        fields = '__all__'


class Pitching_recordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pitching_record
        fields = '__all__'


class Fielding_recordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fielding_record
        fields = '__all__'
