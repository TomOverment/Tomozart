from django.shortcuts import render
from django.views import generic
from .models import Post
from .forms import PostForm, UpdateForm
# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "index.html"
    paginate_by = 6

def profile(request):
    return render(request, 'profile.html')

class AddPostView(generic.CreateView):
    queryset = Post.objects.filter(status=1)
    model = Post
    form_class = PostForm
    template_name = 'addpost.html'
    #fields = '__all__'
    #fields = ('title', 'body', 'author')

class PostDetail(generic.DetailView):
    model = Post
    template_name ="post_detail.html"

class UpdatePost(generic.UpdateView):
    model = Post
    form_class = UpdateForm
    template_name ="editposts.html"
    #fields = ('title', 'content')
