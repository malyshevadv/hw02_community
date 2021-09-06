from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView

from .forms import PostForm
from .models import Group, Post


def index(request):
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'

    posts = Post.objects.all()

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': title,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    title = f'Записи сообщества {group.title}'

    posts = group.posts.all()

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': title,
        'page_obj': page_obj,
    }
    return render(request, template, context)


@login_required
def profile(request, username):
    template = 'posts/profile.html'
    author = get_user_model().objects.get(username=username)
    title = f'Профайл пользователя {author.get_full_name()}'

    posts = Post.objects.filter(author=author)

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': title,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'posts/post_detail.html'
    specific_post = get_object_or_404(Post, pk=post_id)
    title = f'Пост {specific_post.text[0:30]}'

    posts = Post.objects.filter(author=specific_post.author)

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': title,
        'post': specific_post,
        'page_obj': page_obj,
    }
    return render(request, template, context)


@method_decorator(login_required, name='dispatch')
class post_create(CreateView):
    form_class = PostForm
    template_name = 'posts/create_post.html'
    success_url = '/profile/<username>'

    def get_context_data(self, **kwargs):
        context = super(post_create, self).get_context_data(**kwargs)
        context['is_edit'] = False
        return context

    def form_valid(self, form):
        form.instance = form.save(commit=False)
        form.instance.author = self.request.user
        form.instance.save()

        success_url = f'/profile/{self.request.user.username}/'

        return redirect(success_url)


@method_decorator(login_required, name='dispatch')
class post_edit(UpdateView):
    form_class = PostForm
    template_name = 'posts/create_post.html'
    success_url = '/posts/<pk>/'

    def get_object(self, queryset=None):
        return get_object_or_404(Post, pk=self.kwargs['post_id'])

    def get_context_data(self, **kwargs):
        context = super(post_edit, self).get_context_data(**kwargs)
        context['is_edit'] = True
        return context

    def form_valid(self, form):
        form.instance.save()

        success_url = f'/posts/{self.object.pk}/'

        return redirect(success_url)
