import hashlib
from django.conf import settings
from django.db import models


class User(models.Model):
    '''
    User table. Is not necessery to use auth models (too many tables)
    '''
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    is_superadmin = models.BooleanField(default=False)

    def __str__(self):
        '''
        Return string representation of user
        '''
        if self.company:
            return self.company

        if self.first_name or self.last_name:
            return '%s %s' % (self.first_name, self.last_name)

        return self.username

    __unicode__ = __str__

    @staticmethod
    def hashPassword(password):
        h = hashlib.sha256(password.encode('utf8'))
        h.update(settings.SECRET_KEY.encode('utf8'))
        return h.hexdigest()

    def setPassword(self, password):
        self.password = User.hashPassword(password)

    def authenticate(self, password):
        return self.password == User.hashPassword(password)


class Tag(models.Model):
    '''
    Simple tag of Issue, but may be global tags?..
    '''
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    # python2 compatible?
    __unicode__ = __str__


class Issue(models.Model):
    '''
    Specific issue
    '''
    # specify choices enum values
    CH_STATE_OPEN = 1
    CH_STATE_IN_PROGRESS = 2
    CH_STATE_CLOSED = 3

    submitter = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='submitters', blank=True, null=True)
    solver = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='solvers', blank=True, null=True)

    title = models.CharField(max_length=50)
    description = models.TextField()
    # use enum values, can be used with language pack...
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

    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    # python2 compatible?
    __unicode__ = __str__

    def save(self, *args, **kwargs):
        if self.finished is not None and self.duration is None:
            self.duration = (self.finished - self.created).seconds

        return super(Issue, self).save(*args, **kwargs)

