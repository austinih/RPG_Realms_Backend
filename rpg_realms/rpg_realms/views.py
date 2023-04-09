from django.shortcuts import render
from rest_framework import generics
from .models import Publisher, RPG, Review, User, Comment
from .serializers import PublisherSerializer, RPGSerializer, ReviewSerializer
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