from django.urls import path
from .views import PostList, PostDetail, Search,PostCreate, UpdatePost, MyPosts, PostDelete, create_responses, ResponsesDetail, responses
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', cache_page(60)(PostList.as_view())),
    path('posts/', PostList.as_view(), name='post_list'),
    path('posts/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', Search.as_view(), name='search'),
    path('create/', PostCreate.as_view(), name='post_created'),
    path('posts/<int:pk>/update', UpdatePost.as_view(), name='posts_update'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('myposts/', MyPosts.as_view(), name='myposts'),
    path('responses/create/<int:pk>', create_responses, name='responses_create'),
    path('responses/<int:pk>', ResponsesDetail.as_view(), name='responses_detail'),
    path('responses/', responses, name='responses')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
