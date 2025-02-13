from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app.views import HomePageView, CreatePostView
from rest_framework import routers
from app import views

router = routers.DefaultRouter()
router.register(r'post', views.PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='index'),
    path('router/', include(router.urls)),
    path('view/', CreatePostView.as_view(), name='post'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)