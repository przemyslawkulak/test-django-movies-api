from rest_framework import serializers

from api.models import Movie, Director


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('id', 'last_name')


class MovieMiniSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(many=False)

    class Meta:
        model = Movie
        fields = '__all__'
