from django.contrib import admin

# Register your models here.
from .models import NFT
# Register your models here.
@admin.register(NFT)
class NftModel(admin.ModelAdmin):
    list_display=['tokenid','photo_main']