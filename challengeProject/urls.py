"""challengeProject URL Configuration

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

# Should be remove michael

# from django.contrib import admin
from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import url, include
from rest_framework import routers
from CallApi import views
from CallApi.views import RegisterView

router = routers.DefaultRouter()
router.register(r'bills', views.UserViewSet)
router.register(r'calls', views.CallViewSet)
router.register(r'prices', views.GroupViewSet)
router.register(r'album', views.AlbumViewSet)
router.register(r'phone', views.PhoneViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register/', views.RegisterView.get, name='register'),
]

# Include admin url path
urlpatterns += path(settings.ADMIN_URL_PREFIX, admin.site.urls),