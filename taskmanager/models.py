from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    title = models.CharField(max_length=50)


class Issue(models.Model):
    CH_STATE_OPEN = 1
    CH_STATE_IN_PROGRESS = 2
    CH_STATE_CLOSED = 3

    submitter = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='submitters', blank=True, null=True)
    solver = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='solvers', blank=True, null=True)

    title = models.CharField(max_length=50)
    description = models.TextField()
    state = models.IntegerField(
        choices=(
            (CH_STATE_OPEN, 'Open'),
            (CH_STATE_IN_PROGRESS, 'In progress'),
            (CH_STATE_CLOSED, 'Closed'),
        ),
        default=CH_STATE_OPEN,
    )

    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    finished = models.DateTimeField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)

    tags = models.ManyToManyField(Tag)

