from rest_framework import serializers

from api.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'desc', 'year')


class MovieMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
