from django.shortcuts import render_to_response
from django.template import RequestContext

from tagging.models import TaggedItem

from models import Comment
from models import Category
from models import Post
from models import Project

from forms import CommentForm


def home(request):
    """
    Index page
    """
    all_posts = Post.objects.order_by('date_modefied')[:20]
    spotlighted = Post.get_top_rated()
    related = TaggedItem.objects.get_related(all_posts[0], Post)[:6]
    return render_to_response('index.html',
            {
                "posts": all_posts,
                "spotlighted": spotlighted,
                "related": related,
            },
            context_instance=RequestContext(request))


def articles(request):
    """
    Articles page
    """
    all_posts = Post.objects.order_by('date_created')
    categories = Category.objects.all()
    try:
        related = TaggedItem.objects.get_related(all_posts[0], Post)[:6]
    except IndexError:
        related = []
    return render_to_response('articles.html',
            {
                "page_title": "Articles",
                "posts": all_posts,
                "categories": categories,
                "related": related,
            },
            context_instance=RequestContext(request))


def projects(request):
    projects = Project.objects.all()
    posts = Post.objects.all()[:5]
    return render_to_response('projects.html',
                              {
                                "projects": projects,
                                "related_posts": posts,
                              },
                              context_instance=RequestContext(request))


def post(request, post_id, post_name):
    post = Post.objects.get(pk=post_id)
    if request.method == "POST":
        comment_form = CommentForm()
        if comment_form.is_valid():
            comment = Comment()
            comment.author = comment_form.cleaned_data['author']
            comment.post = post
            comment.email = comment_form.cleaned_data['email']
            comment.text = comment_form.cleaned_data['comment']
            comment.save()

    spotlighted = Project.objects.filter(related_posts=post)
    comments = Comment.objects.filter(post=post)
    related = TaggedItem.objects.get_related(post, Post)[:6]
    comment_form = CommentForm()
    return render_to_response('post.html',
            {
                "post": post,
                "comments": comments,
                "related": related,
                "spotlighted": spotlighted,
                "comment_form": comment_form
            },
            context_instance=RequestContext(request))


def project(request, project_id, project_name):
    project = Project.objects.get(pk=project_id)
    related_projects = Project.objects.all()[:5]
    return render_to_response('project.html',
            {
                "project": project,
                "related_projects": related_projects,
            },
            context_instance=RequestContext(request))


def category(request, category):
    try:
        category = Category.objects.get(name= category)
        all_posts = Post.objects.filter(category= category)
        related_posts = TaggedItem.objects.get_related(all_posts[0], Post)[:6]
    except:
        category = Category()
        category.name = "No Articles Yet"
        all_posts = []
        related_posts = []

    categories = Category.objects.all()
    return render_to_response('articles.html',
        {
            "page_title": category.name,
            "page_moto": category.description,
            "posts" : all_posts,
            "categories" : categories,
            "related" : related_posts,
        },
        context_instance=RequestContext(request))


def about(request):
    projects = Project.objects.all()
    post = Post.objects.all()[1]
    return render_to_response('about.html',
            {
                "projects" : projects,
                "post" : post,
            },
            context_instance=RequestContext(request))
