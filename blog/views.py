from django.shortcuts import get_object_or_404, render,redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    posts = Post.objects.all()
    ctx = {'posts': posts}
    return render(request, 'blog/post_list.html', ctx)

def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    ctx = {'post': post}
    return render(request, 'blog/post_detail.html', ctx)

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.create_date = timezone.now()
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    ctx = {'form': form}
    return render(request, 'blog/post_create.html', ctx)

def update(request, post_id):
    update_content = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
      form = PostForm(request.POST, instance=update_content)
      if form.is_valid():
        form.save()
        return redirect('index')
    else:
        form =PostForm(instance=update_content)
    ctx = {'form': form}
    return render(request, 'blog/post_update.html', ctx)

def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('index')