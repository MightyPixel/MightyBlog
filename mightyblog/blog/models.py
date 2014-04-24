from datetime import datetime

from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from redactor.fields import RedactorField
from tagging.fields import TagField
from tagging.utils import parse_tag_input

from mightyblog.settings import base


class PostManager(models.Manager):
    def get_visible(self):
        return super(PostManager, self).get_queryset().filter(visible=True) 

    def get_visible_post(self, post_id):
        try:
            return super(PostManager, self).get_queryset().get(pk=post_id, visible=True) 
        except ObjectDoesNotExist:
            return None


class Post(models.Model):
    title = models.CharField(max_length=127)
    description = models.CharField(max_length=255)
    date_created = models.DateTimeField(default=datetime.now())
    date_modefied = models.DateTimeField(default=datetime.now())
    content = RedactorField()
    tags = TagField()
    visible = models.BooleanField(default=True)

    objects = models.Manager()
    posts = PostManager()

    def __unicode__(self):
        return "%s | (%d,%d,%d)" % (self.title,
                                    self.date_created.day,
                                    self.date_created.month,
                                    self.date_created.year)

    def get_absolute_url(self):
        return "/post/" + str(self.pk) + "/" + self.title.replace(' ', '-')

    def get_tag_list(self):
        return parse_tag_input(self.tags)

    @staticmethod
    def get_top_rated():
        return Post.objects.filter(visible=True)[:10]


class Comment(models.Model):
    author = models.CharField(max_length=63)
    post = models.ForeignKey(Post)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    text = models.TextField(max_length=255)

    def __unicode__(self):
        return "%s: %s.." % (self.author, self.text[:10])



class Category(models.Model):
    name = models.CharField(max_length=63)
    description = models.CharField(max_length=255)
    posts = models.ManyToManyField(Post, null=True, blank=True)
    cover = models.ImageField(null=True, blank=True, upload_to=base.MEDIA_ROOT)
    tags = TagField()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/category/" + self.name.replace(' ', '-')

    def get_cover_url(self):
        print dir(self.cover)
        print self.cover.name
        return self.cover.name.split('/')[-1]


class Project(models.Model):
    name = models.CharField(max_length=63)
    related_posts = models.ManyToManyField(Post, null=True, blank=True)
    github_url = models.URLField(null=True, blank=True)
    content = RedactorField()
    tags = TagField()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/project/" + str(self.pk) + "/" + self.name.replace(' ', '-')

class Friend(models.Model):
    blog = models.URLField(null=True, blank=True)
