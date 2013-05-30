# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Project.text'
        db.delete_column(u'blog_project', 'text')

        # Adding field 'Project.content'
        db.add_column(u'blog_project', 'content',
                      self.gf('tinymce.models.HTMLField')(default=''),
                      keep_default=False)


        # Changing field 'Project.github_url'
        db.alter_column(u'blog_project', 'github_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))
        # Deleting field 'Post.text'
        db.delete_column(u'blog_post', 'text')


    def backwards(self, orm):
        # Adding field 'Project.text'
        db.add_column(u'blog_project', 'text',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Deleting field 'Project.content'
        db.delete_column(u'blog_project', 'content')


        # Changing field 'Project.github_url'
        db.alter_column(u'blog_project', 'github_url', self.gf('django.db.models.fields.URLField')(default='', max_length=200))
        # Adding field 'Post.text'
        db.add_column(u'blog_post', 'text',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    models = {
        u'blog.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'posts': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['blog.Post']", 'null': 'True', 'blank': 'True'}),
            'tags': ('tagging.fields.TagField', [], {})
        },
        u'blog.comment': {
            'Meta': {'object_name': 'Comment'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Post']"}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'blog.post': {
            'Meta': {'object_name': 'Post'},
            'content': ('tinymce.models.HTMLField', [], {}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 4, 22, 0, 0)'}),
            'date_modefied': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 4, 22, 0, 0)'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '127'})
        },
        u'blog.project': {
            'Meta': {'object_name': 'Project'},
            'content': ('tinymce.models.HTMLField', [], {}),
            'github_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'related_posts': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['blog.Post']", 'symmetrical': 'False'}),
            'tags': ('tagging.fields.TagField', [], {})
        }
    }

    complete_apps = ['blog']