from django.db import models

class News(models.Model):
    title = models.CharField(max_length=228)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    audio = models.FileField(upload_to='media/new_audio')


    def __str__(self):
        return self.title