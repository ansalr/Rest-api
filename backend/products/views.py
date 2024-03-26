from rest_framework import generics


from products.models import Product
from products.serializers import ProductSerializers

class productcreateAPIview(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

product_create_view = productcreateAPIview.as_view()

class Productapiview(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

# product_apiview = Productapiview.as_view()
