from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from BLOG_APP import views as blog_views
from BLOG_APP.views import AddPostView, UpdatePost, PostDetail

urlpatterns = [
    path('', blog_views.PostList.as_view(), name='blog'),
    path('admin/', admin.site.urls),
    path('accounts/', include ('allauth.urls')),
    path('accounts/profile/', blog_views.profile, name = 'profile'),
    path('addpost/', AddPostView.as_view(), name= 'add'),
    path('postdetail/<int:pk>', PostDetail.as_view(), name='post-detail'),
    path('updatepost/<int:pk>', UpdatePost.as_view(), name ='update-post')
]
