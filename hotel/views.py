from django.shortcuts import render, redirect
from hotel.models import Room, OrderRoom
from django.utils import timezone
from datetime import datetime


def search_room(request):
    if not request.GET:
        return render(request, "search_room.html")
    datetime(year=2021, month=12, day=9, hour=23, tzinfo=timezone.get_default_timezone())
    start_date = request.GET.get("start_date")
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    start_date = start_date.astimezone(timezone.get_current_timezone())
    end_date = request.GET.get("end_date")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    end_date = end_date.astimezone(timezone.get_current_timezone())
    return redirect("search-room")
