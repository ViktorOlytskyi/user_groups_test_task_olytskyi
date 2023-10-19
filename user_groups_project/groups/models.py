from django.db import models

# groups/models.py
from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def can_delete(self):
        return not self.user_set.exists()

    def __str__(self):
        return self.name