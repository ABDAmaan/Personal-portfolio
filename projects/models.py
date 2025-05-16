from django.db import models
from django.contrib.auth.models import User
from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD




class PostImage(models.Model):
  name = models.CharField(max_length=50)
  image = models.ImageField(upload_to='images/')

  def __str__(self):
    return self.name


class Tags(models.Model):
  name = models.CharField(max_length=20, unique=True)

  def __str__(self):
    return self.name


STATUS = (
  (0, "Draft"),
  (1, "Publish")
  )

class Post(models.Model):
  title = models.CharField(max_length=200, unique=True)
  slug = models.SlugField(max_length=200, unique=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
  summary = models.CharField(max_length=255, null=True)
  tags = models.ManyToManyField(Tags)
  updated_on = models.DateTimeField(auto_now=True)
  body = MarkdownField(rendered_field='body_rendered', validator=VALIDATOR_STANDARD)
  body_rendered = RenderedMarkdownField()
  created_on = models.DateTimeField(auto_now=True)
  status = models.IntegerField(choices=STATUS, default=0)

  class meta:
    ordering = ['-created_on']

  def __str__(self):
    return self.title
  



class Tools(models.Model):
  name = models.CharField(max_length=50, unique=True)

  def __str__(self):
    return self.name


class Project(models.Model):
  title = models.CharField(max_length=200, unique=True)
  tools_used = models.ManyToManyField(Tools)
  description = models.CharField(max_length=225)
  slug = models.SlugField(max_length=200, unique=True)
  body = MarkdownField(rendered_field='body_rendered', validator=VALIDATOR_STANDARD)
  body_rendered = RenderedMarkdownField()
  created_on = models.DateTimeField(auto_now=True)
  updated_on = models.DateTimeField(auto_now=True)
  status = models.IntegerField(choices=STATUS, default=0)

  class meta:
    ordering = ['-created_on']

  def __str__(self):
    return self.title
  

