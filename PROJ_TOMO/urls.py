"""
URL configuration for PROJ_TOMO project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.http import HttpResponse
from django.urls import path, include
from BLOG_APP import views as blog_views
from BLOG_APP.views import AddPostView, EditPostView

urlpatterns = [
    path('', blog_views.PostList.as_view(), name='blog'),
    path('admin/', admin.site.urls),
    path('accounts/', include ('allauth.urls')),
    path('accounts/profile/', blog_views.profile, name = 'profile'),
    path('addpost/', AddPostView.as_view(), name= 'add'),
    path('editpost/<int:pk>', EditPostView.as_view(), name='edit-post'),
]
