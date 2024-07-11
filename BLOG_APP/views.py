from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Post, Comment
from .forms import PostForm, UpdateForm, CommentForm

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "BLOG_APP/index.html"
    paginate_by = 6

def profile(request):
    return render(request, 'BLOG_APP/profile.html')

def about(request):
    return render(request, 'BLOG_APP/about.html')

def gallery(request):
    return render(request, 'BLOG_APP/gallery.html')

class AddPostView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'BLOG_APP/addpost.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        messages.add_message(self.request, messages.SUCCESS, 'Post created successfully!')
        return redirect('home')

def post_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment submitted and awaiting approval')
            return HttpResponseRedirect(request.path_info) 
    else:
        comment_form = CommentForm()
    
    return render(
        request,
        "BLOG_APP/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "form": comment_form  
        }
    )

class PostDetail(generic.DetailView):
    model = Post
    template_name = "BLOG_APP/post_detail.html"

class UpdatePost(generic.UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = "BLOG_APP/editposts.html"




