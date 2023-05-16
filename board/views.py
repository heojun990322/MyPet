from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    page = request.GET.get('page', '1')  # 페이지
    post_list = Post.objects.order_by('-create_date')
    paginator = Paginator(post_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'post_list': page_obj}
    return render(request, 'board/post_list.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'board/post_detail.html', context)

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.create_date = timezone.now()
            post.save()
            return redirect('board:index')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'board/post_form.html', context)