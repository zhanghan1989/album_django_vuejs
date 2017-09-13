from django.db import models

class Album(models.Model):
  title = models.CharField(max_length=32, default='Title')
  content = models.TextField(null=True)
  put_time = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title