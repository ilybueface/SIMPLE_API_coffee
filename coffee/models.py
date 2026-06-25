from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


class Drink(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Order(models.Model):
    class DetailOfOrder(models.TextChoices):
        PENDING = 'PD', 'Pending'
        PREPARING = 'PR', 'Preparing'
        READY = 'RD', 'Ready'
        COMPLETED = 'CP', 'Completed'

    details = models.CharField(
        max_length=200,
        choices=DetailOfOrder.choices,
        default=DetailOfOrder.PENDING,
    )
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')


class Review(models.Model):
    drink = models.ForeignKey(
        Drink,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
            User,
            on_delete=models.SET_NULL,
            null=True,
            blank=True,
    )
    text = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.drink} {self.rating}"


class Promotion(models.Model):
    title = models.CharField(max_length=300)
    discount_percent = models.IntegerField()
    active_until = models.DateField()
    drinks = models.ManyToManyField(Drink)

    def __str__(self):
        return f"{self.title} {self.discount_percent}"


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'drink')

    def __str__(self):
        return f"{self.user} {self.drink}"


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    is_allergen = models.BooleanField()
    extra_price = models.DecimalField(max_digits=6, decimal_places=2)
    drinks = models.ManyToManyField(Drink)

    def __str__(self):
        return f"{self.name} {self.is_allergen} {self.extra_price}"
