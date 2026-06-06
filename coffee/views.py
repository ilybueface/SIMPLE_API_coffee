from django.db.migrations import serializer
from rest_framework import viewsets
from coffee.serilizator import Drinkserializers, Categoryserializers, Orderserializers
from .models import Drink, Category, Order
from rest_framework.decorators import api_view, action
from rest_framework.response import Response


class DrinkViewSet(viewsets.ModelViewSet):
    queryset = Drink.objects.all()
    serializer_class = Drinkserializers

    @action(detail=False, methods=['get'])
    def cheap_drinks(self, request):
        drinks = Drink.objects.filter(price__lt=300)
        drks = Drinkserializers(drinks, many=True)
        return Response(drks.data)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = Categoryserializers

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = Orderserializers

    @action(detail=True, methods=['GET'])
    def today_orders(self, request, pk=None):
        order = self.get_object()
        serializer = Orderserializers(order)
        return Response(serializer.data)

