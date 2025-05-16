from django.shortcuts import render
from django.views import generic
from .models import Post, Project



def index(request):
  latest_blog_post = Post.objects.filter(status=1).order_by("-updated_on")[:3]
  latest_project_post = Project.objects.filter(status=1).order_by("-updated_on")[:3]
  context = {"latest_blog_post":latest_blog_post, "latest_project_post":latest_project_post}
  return render(request, 'index.html', context)
  


class BlogPostListView(generic.ListView):
  template_name = 'blog_post_list.html'
  context_object_name = "blog_post_list"

  def get_queryset(self):
    return Post.objects.filter(status=1).order_by('-created_on')


class ProjectPostListView(generic.ListView):
  template_name = 'project_post_list.html'
  context_object_name = 'project_post_list'

  def get_queryset(self):
    return Project.objects.filter(status=1).order_by('-created_on')



class BlogPostDetailView(generic.DetailView):
  model = Post
  template_name = 'blog_post_detail.html'
  context_object_name = 'post'


class ProjectPostDetailView(generic.DetailView):
  model = Project
  template_name = 'project_post_detail.html'
  context_object_name = 'post'
