from django_filters import FilterSet
                        #ModelChoiceFilter
from .models import Post, Category, PostCategory

class PostFilter(FilterSet):
    class Meta:
       model = Post
       fields = {'title': ['icontains'],
                 'dataCreate': ['gt'],
                 'categoryType': ['exact'],
                 'postCategory': ['exact'],
       }
