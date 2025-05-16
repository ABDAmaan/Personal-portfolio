from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import BlogPostListView , BlogPostDetailView, index, ProjectPostDetailView, ProjectPostListView

urlpatterns = [
  path('', index, name="index"),
  path("blog/", BlogPostListView.as_view(), name="blog_posts"),
  path("<slug:slug>/project/", ProjectPostDetailView.as_view(), name="projects_post_detail"),
  path("projects/", ProjectPostListView.as_view(), name="project_post_list"),
  path("<slug:slug>/blog/", BlogPostDetailView.as_view(), name="blog_post_detail"),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)