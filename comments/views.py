from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.urls import reverse

from .models import Comment
from .forms import CommentForm

class CommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "create_comment.html"
    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.creator_id = self.request.user.id
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('padlock_detail', kwargs={'pk': self.kwargs['pk']})