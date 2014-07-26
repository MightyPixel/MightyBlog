from django.conf.urls import patterns
from django.conf.urls import url


urlpatterns = patterns('blog.views',
    url(r'^$', 'home', name='home'),
    (r'^post/(?P<post_id>\d+)/(?P<post_name>\w+)', 'article'),
    url(r'^project/(?P<project_id>\d+)/(?P<project_name>\w+)', 'project'),
    (r'^category/(?P<category>\w+)', 'category'),
    url(r'^articles/$', 'articles', name='articles'),
    url(r'^projects/$', 'projects', name='projects'),
    url(r'^self/$', 'about', name='about'),
)
