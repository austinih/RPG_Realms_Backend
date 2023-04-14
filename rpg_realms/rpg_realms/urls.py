from django.urls import path
from . import views

urlpatterns = [
    path('', views.PublisherList.as_view(), name='publisher_list'),
    path('publishers/', views.PublisherList.as_view(), name='publisher_list'),
    path('publishers/<int:pk>/', views.PublisherDetail.as_view(), name='publisher_detail'),

    path('rpgs/', views.RPGList.as_view(), name='rpg_list'),
    path('rpgs/<int:pk>/', views.RPGDetail.as_view(), name='rpg_detail'),
    # path('fullrpgs/<int:pk>/', views.FullRPGDetail.as_view(), name='full_rpg_detail'),

    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),

    path('comments/', views.CommentList.as_view(), name='comment_list'),
    path('comments/<int:pk>/', views.CommentDetail.as_view(),name='comment_detail'),
    
    path('reviews/', views.ReviewList.as_view(), name='review_list'),
    path('reviews/<int:pk>/', views.ReviewDetail.as_view(), name='review_detail'),
    path('create-review-detail/', views.ReviewCreateView.as_view(), name='create_review_detail'),
    # path('delete/<int:id>', views.deleteReview, name='deleteReview')
    path('delete-review/', views.ReviewDeleteView.as_view(), name='delete_review_detail')

]