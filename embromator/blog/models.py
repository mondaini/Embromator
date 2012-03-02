from django.db import models

class Tag(models.Model):
    tag = models.CharField(max_length=30)
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __unicode__(self):
        pass

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __unicode__(self):
        return '%s (%s)' % (self.name, self.email)

class Post(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)

class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(Author)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
