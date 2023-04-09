from django.shortcuts import render
from rest_framework import generics
from .models import Publisher, RPG, Review, User, Comment
from .serializers import PublisherSerializer, RPGSerializer, ReviewSerializer, UserSerializer, CommentSerializer
# Create your views here.

class PublisherList(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class RPGList(generics.ListCreateAPIView):
    queryset = RPG.objects.all()
    serializer_class = RPGSerializer

class RPGDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RPG.objects.all()
    serializer_class = RPGSerializer

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer