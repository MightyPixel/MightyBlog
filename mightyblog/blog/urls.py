from django.conf.urls import patterns


urlpatterns = patterns('blog.views',
    (r'^$', 'home'),
    (r'^post/(?P<post_id>\d+)/(?P<post_name>\w+)', 'post'),
    (r'^project/(?P<project_id>\d+)/(?P<project_name>\w+)', 'project'),
    (r'^category/(?P<category>\w+)', 'category'),
    (r'^articles/$', 'articles'),
    (r'^projects/$', 'projects'),
    (r'^self/$', 'about'),
    (r'^tinymce/', include('tinymce.urls')),
)
