from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *


class TBuyerView(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = TBuyerSerializer


class TSellerView(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = TSellerSerializer


class TStockView(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = TStockSerializer


class TItemView(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = TItemSerializer


class TItemsInStockView(viewsets.ModelViewSet):
    queryset = ItemsInStock.objects.all()
    serializer_class = TItemsInStockSerializer


class TItemsForBuyerView(viewsets.ModelViewSet):
    queryset = ItemsForBuyer.objects.all()
    serializer_class = TItemsForBuyerSerializer
