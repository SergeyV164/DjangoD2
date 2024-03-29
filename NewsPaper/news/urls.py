from django.urls import path
from .views import PostsList, PostsDetail, PostCreate, PostUpdate, PostDelete, PostSearch

urlpatterns = [
   path('post/', PostsList.as_view(), name='post_list'),
   path('post/<int:pk>', PostsDetail.as_view(), name='post_detail'),
   path('post/search', PostSearch.as_view(), name='post_search'),
   path('news/create/', PostCreate.as_view(), name='news_create'),
   path('articles/create/', PostCreate.as_view(), name='article_create'),
   path('news/<int:pk>/edit/', PostUpdate.as_view(), name='news_update'),
   path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='article_update'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
   path('articles/<int:pk>/delete/', PostDelete.as_view(), name='article_delete'),
]