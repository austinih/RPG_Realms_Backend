from rest_framework import serializers
from .models import Publisher, RPG, Review, User

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

class UserSerializer(serializers.HyperlinkedModelSerializer):
    reviews = serializers.HyperlinkedRelatedField(
        view_name='review_detail',
        many=True,
        read_only=True
    )
    comments = serializers.HyperlinkedRelatedField(
        view_name='comment_detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = User
        fields = ('id','name','username','email','password','reviews','comments')

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    rpg = serializers.HyperlinkedRelatedField(
        view_name='rpg_detail',
        read_only=True
    )
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )
    comments = serializers.HyperlinkedRelatedField(
        view_name='comment_detail',
        many=True,
        read_only=True
    )
    rpg_id = serializers.PrimaryKeyRelatedField(
        queryset=RPG.objects.all(),
        source='rpg'
    )
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='user'
    )
    class Meta:
        model = Review
        fields = ('id', 'rpg','rpg_id','user','user_id', 'title', 'content', 'score', 'comments')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    review = serializers.HyperlinkedRelatedField(
        view_name='review_detail',
        read_only=True
    )
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )
    review_id = serializers.PrimaryKeyRelatedField(
        queryset=Review.objects.all(),
        source='review'
    )
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='user'
    )
    class Meta:
        model = Review
        fields = ('id', 'review','review_id','user','user_id', 'content')