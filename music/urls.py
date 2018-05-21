from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<pk>/', views.DetailView.as_view(), name='detail'),
    path('album/add/', views.AlbumCreate.as_view(), name='album-add'),
    path('album/<pk>/update', views.AlbumUpdate.as_view(), name='album-update'),
    path('album/<pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),
    path('album/<pk>/addMusic/', views.MusicCreate.as_view(), name='music-create'),
    path('album/<pk>/deleteMusic/', views.MusicDelete.as_view(), name='music-delete'),

]
