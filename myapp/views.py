from django.shortcuts import render, redirect
from myapp.models import Book, RateBookUser, OrderBookUser


def hello(request):
    return render(request, "index.html", {"books": Book.objects.all()})


def add_rate(request, rate, book_id):
    if request.user.is_authenticated:
        RateBookUser.objects.update_or_create(user_id=request.user.id, book_id=book_id, defaults={"rate": rate})
    return redirect("main-page")


def order_book(request, book_id):
    if request.user.is_authenticated:
        OrderBookUser.objects.create(
            count=request.POST.get("count"),
            user_id=request.user.id,
            book_id=book_id
        )
    return redirect("main-page")
