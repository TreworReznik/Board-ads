from django.urls import path, include
from .views import PostList, PostDetail
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>', PostDetail.as_view()),
    path('posts/froala_editor/', include('froala_editor.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

