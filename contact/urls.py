from django.urls import path
from .views import ContactView, ContactSuccessView
from .import views



urlpatterns = [
    path('', ContactView.as_view(), name="contact"),
    path('success/', ContactSuccessView.as_view(), name="success"),
    path('clicked/',views.clicked,name='clicked'),
]