from django.contrib import admin
from .models import RoomRate, OverriddenRoomRate, Discount, DiscountRoomRate

class RoomRateAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'room_name', 'default_rate')
    search_fields = ('room_name',)

class OverriddenRoomRateAdmin(admin.ModelAdmin):
    list_display = ('room_rate', 'overridden_rate', 'stay_date')
    list_filter = ('stay_date',)
    search_fields = ('room_rate__room_name',)

class DiscountAdmin(admin.ModelAdmin):
    list_display = ('discount_id', 'discount_name', 'discount_type', 'discount_value')
    search_fields = ('discount_name',)

class DiscountRoomRateAdmin(admin.ModelAdmin):
    list_display = ('room_rate', 'discount')
    search_fields = ('room_rate__room_name', 'discount__discount_name')

admin.site.register(RoomRate, RoomRateAdmin)
admin.site.register(OverriddenRoomRate, OverriddenRoomRateAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(DiscountRoomRate, DiscountRoomRateAdmin)
