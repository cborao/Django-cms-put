from django.db import models

# Create the content model
class Content(models.Model):

    key = models.CharField(max_length=64)
    value = models.TextField()

    def __str__(self):
        return self.key + ": " + self.value