from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from .forms import EmailPostForm
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/detail.html"
    
def post_share(request, id):
    post = Post.objects.get(id=id)
    if request.method =='POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
    else:
        form = EmailPostForm()
    return render(request, 'blog/share.html' , {
        'post': post,
        'form': form
    })