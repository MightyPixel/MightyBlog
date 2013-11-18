# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Project.content'
        db.alter_column(u'blog_project', 'content', self.gf('redactor.fields.RedactorField')())

        # Changing field 'Post.content'
        db.alter_column(u'blog_post', 'content', self.gf('redactor.fields.RedactorField')())

    def backwards(self, orm):

        # Changing field 'Project.content'
        db.alter_column(u'blog_project', 'content', self.gf('tinymce.models.HTMLField')())

        # Changing field 'Post.content'
        db.alter_column(u'blog_post', 'content', self.gf('tinymce.models.HTMLField')())

    models = {
        u'blog.category': {
            'Meta': {'object_name': 'Category'},
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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
            'content': ('redactor.fields.RedactorField', [], {}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 18, 0, 0)'}),
            'date_modefied': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 18, 0, 0)'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'blog.project': {
            'Meta': {'object_name': 'Project'},
            'content': ('redactor.fields.RedactorField', [], {}),
            'github_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'related_posts': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['blog.Post']", 'symmetrical': 'False'}),
            'tags': ('tagging.fields.TagField', [], {})
        }
    }

    complete_apps = ['blog']