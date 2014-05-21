from django.db.models import Manager

class PostManager(Manager):

    def get_visible(self):
        return super(PostManager, self).get_queryset().filter(visible=True) 

    def get_visible_post(self, post_id):
        try:
            return super(PostManager, self).get_queryset().get(pk=post_id, visible=True) 
        except ObjectDoesNotExist:
            return None

    def get_top_rated(self):
        # TODO implement real rating system ;)
        return super(PostManager, self).get_queryset().filter(visible=True)[:10]


