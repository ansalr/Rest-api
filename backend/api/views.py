import json
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.forms.models import model_to_dict
from products.models import Product
from products.serializers import ProductSerializers


# Create your views here.
# @api_view(['GET'])
# def api_home(request, *args, **kwargs):

#     instance = Product.objects.all().order_by("?").first()
#     data = {}

#     if instance:

#         # data = model_to_dict(instance, fields=['id','title','sale_price'])
#         data = ProductSerializers(instance).data
#     return Response(data)

@api_view(['POST'])
def api_home(request, *args, **kwargs):

    serializer = ProductSerializers(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    
    return Response({"invalid":"invalid Data"},status=400)






        # data['id']=model_data.id
        # data['title']=model_data.title
        # data['content']=model_data.content
        # data['price']=model_data.price

    # return JsonResponse(data)
        # data=dict(data)
        # json_data = json.dumps(data)
        # return HttpResponse(json_data, headers={'content-type':'application/json'})
    # return JsonResponse({'message':"Djangp api response!!"})
