from rest_framework import serializers
from .models import *


class TBuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = ('id', 'url', 'name', 'phone', 'bonus', 'datereg')


class TSellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ('id', 'url', 'seller_name', 'seller', 'phone', 'adres', 'OGRN', 'INN')


class TStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('id', 'url', 'adres', 'maxcap')


class TItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'url', 'seller', 'name', 'avtor', 'ISBN', 'articul', 'PG', 'year', 'pages', 'type', 'format', "mass", 'price')


class TItemsInStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsInStock
        fields = ('id', 'url', 'item', 'stock', 'count')


class TItemsForBuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsForBuyer
        fields = ('id', 'url', 'item', 'buyer', 'count')

