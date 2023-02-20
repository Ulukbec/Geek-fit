from rest_framework import serializers
from geeksfit.models import Training

class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = 'title link description duration category'.split()

class TrainingValidateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField(required=False)
    duration = serializers.CharField()
    category = serializers.CharField()
    link = serializers.CharField()
