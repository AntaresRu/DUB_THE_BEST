from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('Buyer', views.TBuyerView)
router.register('Seller', views.TSellerView)
router.register('Stock', views.TStockView)
router.register('Item', views.TItemView)
router.register('ItemsInStock', views.TItemsInStockView)
router.register('ItemsForBuyer', views.TItemsForBuyerView)

urlpatterns = [
    path('', include(router.urls)),
]
