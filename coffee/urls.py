from coffee.views import DrinkViewSet, OrderViewSet, CategoryViewSet, ReviewViewSet
from django.urls import path
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'drinks', DrinkViewSet, basename='Drink')
router.register(r'order', OrderViewSet, basename='Order')
router.register(r'category', CategoryViewSet, basename='Category')
router.register(r'review', ReviewViewSet, basename='Review')


urlpatterns = router.urls