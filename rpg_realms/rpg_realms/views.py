from django.shortcuts import render
from rest_framework import generics
from .models import Publisher, RPG, Review, User, Comment
from .serializers import PublisherSerializer, RPGSerializer, ReviewSerializer, UserSerializer, CommentSerializer
from django.views.generic import DeleteView
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

# new
# class FullRPGDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = RPG.objects.select_related('publisher')
#     serializer_class = FullRPGSerializer
# New

class RPGDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RPG.objects.select_related('publisher')
    serializer_class = RPGSerializer

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDeleteView(DeleteView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# class ReviewDeleteView(DeleteView):
#     success_message = "Deleted Successfully"
#     def get_queryset(self):
#         qs = super(ReviewDeleteView, self).get_queryset()
#         return qs.filter(owner=self.request.user)
    # model = Review
    # serializer_class = ReviewSerializer
    # success_url = reverse_lazy('venues_list_view')

# def deleteReview(request, id):
#   review = Review.objects.get(id=id)
#   review.delete()
#   return HttpResponseRedirect(reverse('index'))



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