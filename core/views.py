from .models import NFT
from django.http import JsonResponse
MEDIA_URL = '/media/'
def deltailsNFt(request, id):
    nftobj = NFT.objects.get(tokenid=id)
    dictionary = {
        "image": str(nftobj.urlpic) ,
        "tokenId": id,
        "name": 'NFT tutorial' + ' ' + str(id),
        "attributes": []
    }
    return JsonResponse(dictionary)