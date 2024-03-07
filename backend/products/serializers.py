from rest_framework import serializers
from products.models import Product


class ProductSerializers(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model= Product
        fields = [
            'title',
            # 'content',
            'price',
            'discount',
            'sale_price',
        ]
    def get_discount(self, obj):
        print(obj)
        return obj.discount_price()