from django.db import models

# Create your models here.

class Post_a_Jobs(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'post_something_on_homepage_post_a_jobs'
