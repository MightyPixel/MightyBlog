# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table(u'blog_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=127)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 11, 12, 0, 0))),
            ('date_modefied', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 11, 12, 0, 0))),
            ('content', self.gf('tinymce.models.HTMLField')()),
            ('tags', self.gf('tagging.fields.TagField')()),
        ))
        db.send_create_signal(u'blog', ['Post'])

        # Adding model 'Comment'
        db.create_table(u'blog_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=63)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Post'])),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')(max_length=255)),
        ))
        db.send_create_signal(u'blog', ['Comment'])

        # Adding model 'Category'
        db.create_table(u'blog_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=63)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('tags', self.gf('tagging.fields.TagField')()),
        ))
        db.send_create_signal(u'blog', ['Category'])

        # Adding M2M table for field posts on 'Category'
        db.create_table(u'blog_category_posts', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('category', models.ForeignKey(orm[u'blog.category'], null=False)),
            ('post', models.ForeignKey(orm[u'blog.post'], null=False))
        ))
        db.create_unique(u'blog_category_posts', ['category_id', 'post_id'])

        # Adding model 'Project'
        db.create_table(u'blog_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=63)),
            ('github_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('content', self.gf('tinymce.models.HTMLField')()),
            ('tags', self.gf('tagging.fields.TagField')()),
        ))
        db.send_create_signal(u'blog', ['Project'])

        # Adding M2M table for field related_posts on 'Project'
        db.create_table(u'blog_project_related_posts', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'blog.project'], null=False)),
            ('post', models.ForeignKey(orm[u'blog.post'], null=False))
        ))
        db.create_unique(u'blog_project_related_posts', ['project_id', 'post_id'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table(u'blog_post')

        # Deleting model 'Comment'
        db.delete_table(u'blog_comment')

        # Deleting model 'Category'
        db.delete_table(u'blog_category')

        # Removing M2M table for field posts on 'Category'
        db.delete_table('blog_category_posts')

        # Deleting model 'Project'
        db.delete_table(u'blog_project')

        # Removing M2M table for field related_posts on 'Project'
        db.delete_table('blog_project_related_posts')


    models = {
        u'blog.category': {
            'Meta': {'object_name': 'Category'},
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
            'content': ('tinymce.models.HTMLField', [], {}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 12, 0, 0)'}),
            'date_modefied': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 12, 0, 0)'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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