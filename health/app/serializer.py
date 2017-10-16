from rest_framework import serializers
from app.models import *


class CitasSerializer(serializers.Serializer):

	id=serializers.IntegerField()
	start=serializers.CharField()
	end=serializers.CharField()
	title=serializers.CharField()
	descripcion=serializers.CharField()

	def update(self, instance, validated_data):
		"""
		Update and return an existing `Snippet` instance, given the validated data.
		"""
		instance.start = validated_data.get('start', instance.start)
		instance.end = validated_data.get('end', instance.end)
		instance.title = validated_data.get('title', instance.title)
		instance.descripcion = validated_data.get('descripcion', instance.descripcion)
		instance.save()
		return instance