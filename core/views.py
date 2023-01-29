from .models import NFT
from django.http import JsonResponse
MEDIA_URL = '/media/'
def deltailsNFt(request, id):
    nftobj = NFT.objects.get(id=id)
    dictionary = {
        "image": 'https://nftbackend.onrender.com/media/' + str(nftobj.photo_main) ,
        "tokenId": id,
        "name": 'NFT tutorial' + ' ' + str(id),
        "attributes": []
    }
    return JsonResponse(dictionary)
