from django.db import models

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
        
class Review(models.Model):
    review_title = models.CharField('Review Title', max_length=30)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField('Score')
    comment = models.CharField('Review Comment', max_length=300)
    
    def __str__(self):
        return self.review_title