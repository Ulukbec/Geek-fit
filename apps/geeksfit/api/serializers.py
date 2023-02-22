from rest_framework import serializers
from apps.geeksfit.models import Training, Category, Review
from rest_framework.relations import PrimaryKeyRelatedField


class CategorySerializer(PrimaryKeyRelatedField, serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ReviewSerializer(PrimaryKeyRelatedField, serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'stars'.split()


class TrainingSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, queryset=Category.objects.all())
    reviews = ReviewSerializer(many=True, queryset=Review.objects.all())

    class Meta:
        model = Training
        fields = 'title duration category reviews'.split()
