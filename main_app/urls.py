from django.urls import path

from . import views

urlpatterns = [


    path('', views.Index.as_view(), name ="index"),
    path('profile/<int:pk>/', views.ProfileDetail.as_view(), name ="profile_detail"),
    path('post-show', views.PostShow.as_view(), name='post-show'),
    path('cities', views.Cities.as_view(), name='cities'),
    path('user-public', views.UserPublic.as_view(), name='user')
    # path('profile/<int:pk>/posts/<int:pk>')
]

