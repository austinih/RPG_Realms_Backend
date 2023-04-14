from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=100)
    website_url = models.TextField()
    logo_url = models.TextField()
    is_indie = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)
    
class RPG(models.Model):
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='rpgs')
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    image_url = models.TextField()

    def __str__(self):
        return str(self.title)

class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.TextField()
    email = models.CharField(max_length=100)
    password = models.TextField()

    def __str__(self):
        return str(self.name)
    
class Review(models.Model):
    rpg = models.ForeignKey(RPG, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateField(null = True)
    score = models.IntegerField(
        default=5,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
)

    def __str__(self):
        return str(self.title)
    
class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()

    def __str__(self):
        return str(self.content)