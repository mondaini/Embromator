from django.db import models

class Post(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=20)
    text = models.TextField()
    tags = ListField()
    comments = ListField(EmbeddedModelField('Comment'))

class Comment(models.Model):
	created_on = models.DateTimeField(auto_now_add=True)
	author = EmbeddedModelField('Author')
	text = models.TextField()

class Author(models.Model):
	name = models.CharField(max_length=20)
	email = models.EmailField()

	def __unicode__(self):
		return '%s (%s)' % (self.name, self.email)

class Tag(models.Model):
	tag = models.CharField(max_length=20)
    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    def __unicode__(self):
        pass
    