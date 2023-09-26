from django.urls import path, include
from .views import PostList, PostDetail, Search, UserResponses, PostCreate, UpdatePost, MyPosts
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', cache_page(60)(PostList.as_view())),
    path('posts/', PostList.as_view(), name='post_list'),
    path('posts/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', Search.as_view(), name='search'),
    path('responses/', UserResponses.as_view(), name='responses'),
    path('create/', PostCreate.as_view(), name='post_created'),
    path('posts/<int:pk>/update', UpdatePost.as_view(), name='posts_update'),
    path('myposts/', MyPosts.as_view(), name='myposts'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
