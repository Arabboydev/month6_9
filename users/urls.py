from django.url import path
from .views import LondingPageView


urlpatterns = [
    path("",LondingPageView.as_view(), name="landing"),
]