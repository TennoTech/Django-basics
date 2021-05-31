from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('search/', views.post_search, name='search'),
    path('category/<category>/', views.CatListView.as_view(), name='category'),
    path('<slug:post>/', views.post_single, name='post_single'),
]