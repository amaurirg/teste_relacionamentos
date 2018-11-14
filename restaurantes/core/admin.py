from django.contrib import admin
from restaurantes.core.models import Place, Restaurant, Waiter


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('place_id', 'place', 'serves_hot_dogs', 'serves_pizza')#, 'place_address')


class WaiterAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'name')
    list_select_related = ('restaurant')


admin.site.register(Place, PlaceAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Waiter, WaiterAdmin)
