from django.urls import path
from . import views

urlpatterns = [
    path('', views.PublisherList.as_view(), name='publisher_list'),
    path('publishers/', views.PublisherList.as_view(), name='publisher_list'),
    path('rpgs/', views.RPGList.as_view(), name='rpg_list'),
    path('reviews/', views.ReviewList.as_view(), name='review_list'),
    path('users/', views.UserList.as_view(), name='user_list'),
    path('comments/', views.CommentList.as_view(), name='comment_list'),
    path('publishers/<int:pk>/', views.PublisherDetail.as_view(), name='publisher_detail'),
    path('rpgs/<int:pk>/', views.RPGDetail.as_view(), name='rpg_detail'),
    path('reviews/<int:pk>/', views.ReviewDetail.as_view(), name='review_detail'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name='comment_detail'),
]