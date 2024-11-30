from django.urls import path
from .views import PostsList, PostsDetail, PostCreate, PostUpdate, PostDelete, PostSearch, subscriptions
from django.views.decorators.cache import cache_page


#CategoryListView, subscribe
urlpatterns = [
   path('post/', PostsList.as_view(), name='post_list'),
   path('post/<int:pk>', cache_page(300)(PostsDetail.as_view()), name='post_detail'),
   path('post/search', PostSearch.as_view(), name='post_search'),
   path('news/create/', cache_page(300)(PostCreate.as_view()), name='news_create'),
   path('articles/create/', cache_page(300)(PostCreate.as_view()), name='article_create'),
   path('news/<int:pk>/edit/', cache_page(300)(PostUpdate.as_view()), name='news_update'),
   path('articles/<int:pk>/edit/', cache_page(300)(PostUpdate.as_view()), name='article_update'),
   path('news/<int:pk>/delete/', cache_page(300)(PostDelete.as_view()), name='news_delete'),
   path('articles/<int:pk>/delete/', cache_page(300)(PostDelete.as_view()), name='article_delete'),
   path('subscriptions/', subscriptions, name='subscriptions'),

   #path('subscriptions/<int:pk>', CategoryListView.as_view(), name='subscriptions'),
   #path('subscriptions/<int:pk>/subscribe', subscribe, name='subscribe'),
]