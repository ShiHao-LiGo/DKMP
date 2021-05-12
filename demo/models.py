from django.db import models

# Create your models here.
from django.db import models
class Datas(models.Model):
    Bug_ID = models.CharField(max_length=30)
    title = models.TextField(null=True)
    product = models.TextField(null=True)
    component = models.TextField(null=True)
    Type = models.TextField(null=True)
    Priority = models.TextField(null=True)
    Severity = models.TextField(null=True)
    Status = models.TextField(null=True)
    Milestone = models.TextField(null=True)
    comment = models.TextField(null=True)
    def __str__(self):
        return self.Bug_ID

