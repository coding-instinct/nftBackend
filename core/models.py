from django.db import models

# Create your models here.
class NFT(models.Model):
    tokenid = models.IntegerField(null= False , unique= True)
    urlpic = models.URLField( max_length=200, null = True)