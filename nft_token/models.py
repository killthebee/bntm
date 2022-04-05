import os

from django.db import models
from binascii import hexlify


def create_hash():
    return hexlify(os.urandom(10))


class Token(models.Model):
    unique_hash = models.CharField(max_length=20, default=create_hash, unique=True)
    tx_hash = models.CharField(max_length=50, unique=True)
    media_url = models.CharField(
        max_length=200,
        default="https://squeaksandnibbles.com/wp-content/uploads/2018/02/Peruvian-Guinea-Pig-Breed-Information-SN-long.jpg"
    )
    owner = models.CharField(max_length=50)


