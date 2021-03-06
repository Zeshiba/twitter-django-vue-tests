"""twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path

from rest_framework.routers import DefaultRouter

from rest_framework_jwt.views import obtain_jwt_token

from twitter import views


router = DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)
router.register(r'tweets', views.TweetViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/me/', views.CurrentUserView.as_view()),
    path('api/users/<str:username>/', views.ProfileView.as_view()),
    path('api/users/<str:username>/tweets/',
         views.UserTweetsView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('api-auth/register/', views.RegisterView.as_view()),
    path('api-token-auth/', obtain_jwt_token),
    re_path(r'^(.*/)?$', views.FrontendView.as_view()),
]
