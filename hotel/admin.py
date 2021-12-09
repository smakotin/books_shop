from django.contrib import admin
from hotel.models import Room, OrderRoom


class OrderRoomInline(admin.StackedInline):
    model = OrderRoom
    readonly_fields = ['price']


class RoomAdmin(admin.ModelAdmin):
    inlines = [OrderRoomInline]


admin.site.register(Room, RoomAdmin)
