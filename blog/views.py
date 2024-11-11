from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Post, Comment

# Post List View
class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(status='published').select_related('author')

# Post Detail View
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

# Comment Create View
class CommentCreateView(CreateView):
    model = Comment
    fields = ['content']
    template_name = 'comment_form.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
