from django.urls import path
from .views import PostListView, PostDetail


app_name="blogapi"

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('', PostListView.as_view(), name='listcreate')
] 