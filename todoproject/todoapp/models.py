from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=20)
    description=models.CharField(max_length=256)
    status=models.CharField(max_length=20)
    date_time=models.CharField(max_length=64)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
