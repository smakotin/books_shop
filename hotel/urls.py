from django.urls import path
from hotel.views import search_room


urlpatterns = [
    path("serach_room/", search_room, name="search-room"),
]
