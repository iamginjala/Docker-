from django.db import models

class Tasks(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    due_date = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)  # Change this to auto_now=True
    progress = models.IntegerField(default=0)

    def __str__(self):
        return self.title
