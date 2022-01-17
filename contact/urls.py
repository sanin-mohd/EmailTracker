
from django.urls import path,re_path
from .views import ContactView, ContactSuccessView
from .import views



urlpatterns = [
    path('', ContactView.as_view(), name="contact"),
    path('success/', ContactSuccessView.as_view(), name="success"),
    path('track/<str:event_id>',views.track,name='track'),
    path('link',views.link,name='link'),
    
]