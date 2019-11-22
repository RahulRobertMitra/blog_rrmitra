from django.conf import settings
from django.db import models
from django.utils import timezone



class Topic(models.Model):
    name = models.CharField(
       max_length=50,
       unique= True
    )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status=self.model.PUBLISHED)

    def draft(self):
        return self.filter(status=self.model.DRAFT)

class Post(models.Model):
    """
    Represents a blog post
    """
    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    ]

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # The Django auth user model
        on_delete=models.PROTECT,  # Prevent posts from being deleted
        related_name='blog_posts',  # "This" on the user model
        null=True,
    )

    title = models.CharField(max_length=255)
    status = models.CharField(
         max_length =10,
         choices=STATUS_CHOICES,
         default = DRAFT,
         help_text='Set to "Published" to make public'
)

    slug = models.SlugField(
         null=True,
         unique_for_date='published',



    )
    topics = models.ManyToManyField(
        Topic,
        related_name='blog_posts'
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)  # Sets on create
    updated = models.DateTimeField(auto_now=True)  # Updates on each save
    published = models.DateTimeField(
        null =True,
        blank=True,
        help_text ='the publishing date'

    )
    objects = PostQuerySet.as_manager()

    class Meta:
         ordering = ['-created']

    def __str__(self):
        return self.title

class Comment(models.Model):
   """
   Represents a blog post
   """
   #Post = models.CharField(max_length=255)
   Post = models.ForeignKey(
       Post,
       on_delete=models.PROTECT,
       related_name='comments',
       null=True
   )

   Name = models.CharField(max_length=255)
   Email = models.CharField(max_length=50)
   Text = models.TextField()
   Approved = models.BooleanField(default=True)
   created = models.DateTimeField(auto_now_add=True)  # Sets on create
   updated = models.DateTimeField(auto_now=True)  # Updates on each saver models here.



   def __str__(self):
       return self.Name


   def publish(self):
    #    self.status=self.PUBLISHED
    #    self.published = timezone.now()
      pass
