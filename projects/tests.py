from django.test import TestCase
from django.urls import reverse
from .models import Post, Project, User

class IndexTest(TestCase):
  def setUp(self):
    self.user = User.objects.create_user(username='test',email='amaan@gmail.com', password='testpassword')
    Post.objects.create(title="Visible", status=1, author=self.user, slug="visible")
    Post.objects.create(title='hidden', status=0, author=self.user, slug="hidden")
    Project.objects.create(title="is visible", status=1, slug="is-visible")
    Project.objects.create(title='not visible', status=0, slug="not-visible")


  def test_return_post_successfully(self):
    response = self.client.get(reverse('blog_posts'))
    self.assertEqual(response.status_code, 200)

    articles = response.context['blog_post_list']
    self.assertEqual(len(articles),1)
    self.assertEqual(articles[0].title, "Visible")

    self.assertContains(response, "Visible")
    self.assertNotContains(response, "hidden")

  def test_index_display_only_published(self):
    response = self.client.get(reverse('index'))
    self.assertEqual(response.status_code, 200)

    latest_blog = response.context["latest_blog_post"]
    latest_project = response.context["latest_project_post"]
    self.assertEqual(len(latest_blog),1)
    self.assertEqual(latest_blog[0].title,"Visible")
    self.assertEqual(len(latest_project), 1)
    self.assertEqual(latest_project[0].title,"is visible" )

    self.assertContains(response, "Visible")
    self.assertContains(response, "is visible")
    self.assertNotContains(response, "hidden")
    self.assertNotContains(response, "not visible")

  
class DetailViewTest(TestCase):
  def setUp(self):
    self.user = User.objects.create_user(username='test',email='amaan@gmail.com', password='testpassword')
    Project.objects.create(title="Project 1", slug="project-1", status=1)
    Post.objects.create(title="Blog 1", slug="blog-1", author=self.user, status=1)

  def test_detailview_returns_correct_post(self):
    project_response = self.client.get(reverse('projects_post_detail', kwargs={"slug":"project-1"}))
    blog_response = self.client.get(reverse('blog_post_detail', kwargs={"slug":"blog-1"}))


    self.assertContains(project_response, "Project 1")
    self.assertNotContains(project_response, "Blog 1")
    self.assertContains(blog_response, "Blog 1")
    self.assertNotContains(blog_response, "Project 1")