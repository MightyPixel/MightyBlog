# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Comment.email'
        db.add_column(u'blog_comment', 'email',
                      self.gf('django.db.models.fields.CharField')(max_length=63, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Comment.website'
        db.add_column(u'blog_comment', 'website',
                      self.gf('django.db.models.fields.CharField')(max_length=63, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Comment.email'
        db.delete_column(u'blog_comment', 'email')

        # Deleting field 'Comment.website'
        db.delete_column(u'blog_comment', 'website')


    models = {
        u'blog.comment': {
            'Meta': {'object_name': 'Comment'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '63', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Post']"}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '63', 'null': 'True', 'blank': 'True'})
        },
        u'blog.post': {
            'Meta': {'object_name': 'Post'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 3, 28, 0, 0)'}),
            'date_modefied': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 3, 28, 0, 0)'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '127'})
        }
    }

    complete_apps = ['blog']