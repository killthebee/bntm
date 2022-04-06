from django.db import models


class Token(models.Model):
    unique_hash = models.CharField(max_length=30, unique=True)
    tx_hash = models.CharField(max_length=100, unique=True)
    media_url = models.CharField(
        max_length=200,
        default="https://squeaksandnibbles.com/wp-content/uploads/2018/02/Peruvian-Guinea-Pig-Breed-Information-SN-long.jpg"
    )
    owner = models.CharField(max_length=50)
