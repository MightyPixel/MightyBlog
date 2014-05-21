import models

from django import forms
from django.contrib import admin

from redactor.widgets import RedactorEditor


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = models.Post
        widgets = {
           'content': RedactorEditor(),
        }


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment)
admin.site.register(models.Project)
admin.site.register(models.Category)
