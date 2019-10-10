from django.conf import settings
from django.db import models

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
        null=False,
    )

    title = models.CharField(max_length=255)
    status = models.CharField(
         max_length =10,
         choices=STATUS_CHOICES,
         default = DRAFT,
         help_text='Set to "Published" to make public'
)

    slug = models.SlugField(
         null=False,
         unique_for_date='published',


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
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
