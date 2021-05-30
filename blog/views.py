from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from .forms import NewCommentForm
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    all_posts = Post.newmanager.all()
    return render(request, 'index.html', {'posts': all_posts})


def post_single(request, post):
    post = get_object_or_404(Post, slug=post, status='published')

    allcomments = post.comments.filter(status=True)
    page = request.GET.get('page', 1)
    paginator = Paginator(allcomments, 3)

    try: 
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)
    
    user_comment = None

    if request.method == 'POST':
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            # gets current post
            user_comment.post = post
            user_comment.save()
            return redirect('/' + post.slug)

    # show the comment form
    comment_form = NewCommentForm()
    context = {
        'post': post,
        'user_comments': user_comment,
        'comments': comments,
        'comment_form': comment_form,
        'allcomments': allcomments
    }
    return render(request, 'single.html', context)


class CatListView(ListView):
    template_name = 'category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat':
            self.kwargs['category'],
            'posts':
            Post.objects.filter(category__name=self.kwargs['category']).filter(
                status='published')
        }
        return content


def category_list(request):
    category = Category.objects.exclude(name='default')
    context = {'category_list': category}
    return context
