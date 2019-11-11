from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class PublishedManager(models.Manager):
    """
    デフォルトで公開中のもののみを取得
    """
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter("published")

class Article(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    ###### マネージャー ####################################################
    
    objects = models.Manager()             # 見えていないが実際にはこれがある
    published = PublishedManager()

    ########################################################################
    ###### フィールド定義 ##################################################

    title = models.CharField(max_length=250) 
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_articles')
    body = models.TextField() 
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    ########################################################################
    class Meta:
        ordering = ('-publish',) 

    def __str__(self):
        return self.title