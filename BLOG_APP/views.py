from django.shortcuts import render
from django.views import generic
from .models import Post
# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "index.html"
    paginate_by = 4

def profile(request):
    return render(request, 'profile.html')

class AddPostView(generic.CreateView):
    queryset = Post.objects.filter(status=1)
    model = Post
    template_name = 'addpost.html'
    fields = '__all__'
    #fields = ('title', 'body', 'author')
