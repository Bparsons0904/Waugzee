from django.db import models

class WishList(models.Model):
    """Model for the individual Wish List's"""
    name = models.TextField(max_length=50)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Wish List'

class Event(models.Model):
    """Event details"""
    date = models.DateField('Event Date')
    time = models.TimeField()
    location = models.TextField(max_length=50)
    wishlist = models.ForeignKey(WishList, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.location

    class Meta:
        verbose_name = 'Wish List Event'

class Items(models.Model):
    """Wishlist Items"""
    name = models.TextField(max_length=50)
    store = models.TextField(max_length=50, null=True, blank=True)
    url = models.TextField(max_length=150, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    wishlist = models.ForeignKey(WishList, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Wish List Item'
