from django.db import models

# Create your models here.
class Article(models.Model) :
    title = models.CharField(max_length = 100)
#titile of blog
    category = models.CharField(max_length = 50, blank = True)
#category of blog
    date_time = models.DateTimeField(auto_now_add = True)
#date of blog
    content = models.TextField(blank = True, null = True)
#content

    def __str__(self) :
        return self.title
    
    class Meta:
        ordering = ['-date_time']
