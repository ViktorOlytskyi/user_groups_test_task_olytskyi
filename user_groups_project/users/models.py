from django.db import models

# users/models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey('groups.Group', on_delete=models.SET_NULL, null=True)



