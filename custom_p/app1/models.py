from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('auth.User',on_delete = models.CASCADE,related_name="blogs")
