from rest_framework import serializers
from .models import Publisher, RPG, Review

class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    rpgs = serializers.HyperlinkedRelatedField(
        view_name='rpg_detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = Publisher
        fields = ('id','name','website_url','logo_url','is_indie','rpgs')

class RPGSerializer(serializers.HyperlinkedModelSerializer):
    publisher = serializers.HyperlinkedRelatedField(
        view_name='publisher_detail',
        read_only=True
    )
    publisher_id = serializers.PrimaryKeyRelatedField(
        queryset=Publisher.objects.all(),
        source='publisher'
    )
    class Meta:
        model = RPG
        fields = ('id', 'publisher','publisher_id', 'title', 'description', 'genre','image_url',)

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    rpg = serializers.HyperlinkedRelatedField(
        view_name='rpg_detail',
        read_only=True
    )
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )
    # rpg_id = serializers.PrimaryKeyRelatedField(
    #     queryset=Publisher.objects.all(),
    #     source='publisher'
    # )
    class Meta:
        model = Review
        fields = ('id', 'rpg','user', 'title', 'content', 'score')