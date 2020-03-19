from django.urls import path
from .views import SchoolDataParseView

urlpatterns = [
    path(r'data/', SchoolDataParseView.as_view(), name="school_data"),
]