from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post-list/', views.mitushchapchapListView.as_view(), name='post-list')
]