from django.db import models

# Create your models here.
class Template(models.Model):
    title = models.CharField('Template Title', max_length =30)
    description = models.TextField()
    image_url = models.CharField('Template Image Url', max_length = 300)
    color = models.CharField('Template Color', max_length = 10)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def mean_rating(self):
        self.reviews.all() # get all ratings
        
    def __str__(self):
        return self.title

        # then compute mean rating and return it
        
class User(models.Model):
    name = models.CharField("User's Name", max_length=30)
    
    def __str__(self):
        return self.name