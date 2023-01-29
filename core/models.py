from django.db import models

# Create your models here.
class NFT(models.Model):
    tokenid = models.IntegerField(null= False , unique= True)
    photo_main = models.ImageField(upload_to='nftimg/%Y/%m/%d/', blank = True)