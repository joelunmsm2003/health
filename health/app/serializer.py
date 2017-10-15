from rest_framework import serializers
from app.models import *


class CitasSerializer(serializers.Serializer):

    start=serializers.CharField()
    end=serializers.CharField()
    title=serializers.CharField()