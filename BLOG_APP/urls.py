from django.urls import path
from . import views
from .views import delete_post

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('addpost/', views.AddPostView.as_view(), name='add_post'),
    path('post/edit/<int:pk>/', views.UpdatePost.as_view(), name='update_post'),
    path('postdetail/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('blog/', views.PostList.as_view(), name='blog'),
    path('post/<int:post_id>/delete/', delete_post, name='delete_post'),
    path('art-gallery/', views.art_gallery, name='art_gallery'),
]





