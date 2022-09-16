from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView
from .models import Blog, BlogContent, STATUS_PUBLISH, STATUS_DRAFT
from django.core.paginator import Paginator
from django.views import generic
from newsletter.forms import SubscibersForm, MailMessageForm
from django.contrib import messages


class BlogList(generic.ListView):
    paginate_by = '6'
    queryset = Blog.objects.filter(status=STATUS_PUBLISH).order_by('-publish_date')
    template_name = 'blog/blog.html'
    context_object_name='posts'
    
class BlogDetails(generic.DetailView):
    model = Blog
    template_name= 'blog/detail.html'
    
def detail_view(request,slug):
    section = get_object_or_404(Blog, slug=slug)
    content = BlogContent.objects.filter(section=section)
    post = Blog.objects.filter(status=STATUS_PUBLISH).order_by('-publish_date')[0:5]
    if request.method == 'POST':
        form = SubscibersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscription Successful')
            return redirect('blog:blog-detail', slug=slug)
    else:
        form = SubscibersForm()
 
    return render(request, 'blog/detail.html', {'content':content, 'section':section, 'post':post, 'form':form,})
