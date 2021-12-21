from django.urls import path
from .views import ContactView, ContactSuccessView
from .import views

app_name = 'contact'

urlpatterns = [
    path('', ContactView.as_view(), name="contact"),
    path('success/', ContactSuccessView.as_view(), name="success"),
    path('clicked/',views.clicked,name='clicked'),
]