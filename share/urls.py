
from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name ="share.home"),
    path('share/', views.CreatePhotoView.as_view(), name ="share.post"),
     path('photo/<int:pk>/update/', views.UpdatePhotoView.as_view(), name ="share.update"),
     path('photo/<int:pk>/delete/', views.PhotoDeleteView.as_view(), name ="share.delete"),
     path('like/', views.photo_like, name="share.like"),
]
