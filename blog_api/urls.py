from django.urls import path
from rest_framework import urlpatterns
from .views import PostList, PostDetail, PostSearch, PostListDetailfilter
from rest_framework.routers import DefaultRouter
# from .views import PostList, PostDetail

app_name= 'blog_api'

# urlpatterns = [
#     path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
#     path('', PostList.as_view(), name='listcreate')
# ]

# router = DefaultRouter()
# router.register('', PostList, basename='user')
# urlpatterns = router.urls
urlpatterns = [
    path('posts/<str:pk>', PostDetail.as_view(), name='detailcreate'),
    path('search/', PostListDetailfilter.as_view(), name='postsearch'),
    path('', PostList.as_view(), name='listcreate'),
]