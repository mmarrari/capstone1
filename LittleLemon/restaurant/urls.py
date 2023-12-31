# define URL route for index() view
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"tables", views.BookingViewSet)


urlpatterns = [
    path("", views.index, name="index"),
    path("menu/<int:pk>/", views.SingleMenuItemView.as_view()),
    path("booking/", include(router.urls)),
]
