from django.urls import path
from myapp import views


urlpatterns = [
    path("hello/", views.hello, name="main-page"),
    path("add_rate/<int:rate>/<int:book_id>/", views.add_rate, name="add-rate"),
    path("order_book/<int:book_id>/", views.order_book, name="order-book"),
    path("delete_book/<int:book_id>/", views.delete_book, name="delete-book"),
    path("update_book/<int:book_id>/", views.update_book, name="update-book"),
    path("add_comment/<int:book_id>/", views.add_comment, name="add-comment"),
    path("delete_comment/<int:comment_id>/", views.delete_comment, name="delete-comment"),
    path("update_comment/<int:comment_id>/", views.update_comment, name="update-comment"),
    path("my_account/", views.my_account, name="my-account"),
    path("logout/", views.logout_view, name="logout"),
    path("login/", views.login_view, name="login")
]
