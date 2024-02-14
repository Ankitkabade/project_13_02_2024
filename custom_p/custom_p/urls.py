
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from app1.views import BlogViewSet
from auth_app.views import UserViewSet
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

router = DefaultRouter()
router.register('blogs', BlogViewSet, basename='blogs')
router.register('user', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
     path('v1/', include(router.urls)),
     path('access/',token_obtain_pair),
     path('refresh/',token_refresh),

]
