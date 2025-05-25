from django.db import models
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel
from core import utils


# Create your models here.


class Repository(TimeStampedModel):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.name


class Commit(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='commits')
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    code = models.TextField()
    hash = models.CharField(max_length=40, default=utils.generate_hash) # Generate hash if one isn't passed

    def __str__(self):
        return f'commit {self.hash}'
