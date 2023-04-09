from rest_framework import serializers
from .models import Publisher, RPG, Review, User

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
    review_url = serializers.ModelSerializer.serializer_url_field(
        view_name='review_detail'
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
        fields = ('id', 'rpg','rpg_id','user','user_id', 'title', 'content', 'score', 'comments','review_url')

class RPGSerializer(serializers.HyperlinkedModelSerializer):
    publisher = serializers.HyperlinkedRelatedField(
        view_name='publisher_detail',
        read_only=True
    )
    reviews = ReviewSerializer(
        many=True,
        read_only=True
    )
    rpg_url = serializers.ModelSerializer.serializer_url_field(
        view_name='rpg_detail'
    )
    publisher_id = serializers.PrimaryKeyRelatedField(
        queryset=Publisher.objects.all(),
        source='publisher'
    )
    class Meta:
        model = RPG
        fields = ('id', 'publisher','publisher_id', 'title', 'description', 'genre','image_url','rpg_url','reviews')

class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    rpgs = RPGSerializer(
        many=True,
        read_only=True
    )
    publisher_url = serializers.ModelSerializer.serializer_url_field(
        view_name='publisher_detail'
    )
    class Meta:
        model = Publisher
        fields = ('id','name','website_url','logo_url','is_indie','publisher_url','rpgs')



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
    user_url = serializers.ModelSerializer.serializer_url_field(
        view_name='user_detail'
    )
    class Meta:
        model = User
        fields = ('id','name','username','email','password','reviews','comments','user_url')



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
    comment_url = serializers.ModelSerializer.serializer_url_field(
        view_name='comment_detail'
    )
    class Meta:
        model = Review
        fields = ('id', 'review','review_id','user','user_id', 'content','comment_url')