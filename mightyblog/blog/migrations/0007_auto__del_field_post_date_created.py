# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Post.date_created'
        db.delete_column(u'blog_post', 'date_created')


    def backwards(self, orm):
        # Adding field 'Post.date_created'
        db.add_column(u'blog_post', 'date_created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 3, 26, 0, 0), null=True),
                      keep_default=False)


    models = {
        u'blog.comment': {
            'Meta': {'object_name': 'Comment'},
            'author': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '63', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Post']"}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '255'})
        },
        u'blog.post': {
            'Meta': {'object_name': 'Post'},
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '63', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '127'})
        }
    }

    complete_apps = ['blog']