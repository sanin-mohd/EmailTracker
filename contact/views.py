
from django.shortcuts import render
from django.http import HttpResponse
from time import gmtime, strftime, timezone
from django.views.generic import FormView, TemplateView
import datetime
from contact.models import EmailEventDatabase, Ip
from .forms import ContactForm
from django.urls import reverse_lazy
import pygeoip
from django.conf import settings
import ipinfo
# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
@method_decorator(csrf_exempt, name='dispatch')
class ContactView(FormView):

    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        
        return super().form_valid(form)


class ContactSuccessView(TemplateView):
    
    template_name = 'contact/success.html'
    def get_context_data(self, **kwargs):
       context = super(ContactSuccessView, self).get_context_data(**kwargs)
       # here's the difference:
       context['datas'] = EmailEventDatabase.objects.all()
       return context

def track(request,event_id):
    
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    try:
        email_event=EmailEventDatabase.objects.get(id=event_id)
        email_event.no_of_opening+=1
        email_event.last_opening_time=datetime.datetime.today()
        email_event.last_used_ip=ip
        email_event.last_location='--'
        email_event.save()
        ip_details=Ip()
        ip_details.email_event=email_event
        ip_details.ip=ip
        ip_details.save()
        print(f'{email_event.email}')
        print("Email Opened")
        print(f'IP address :{ip}')
        showtime = datetime.datetime.today()
        print(f'Time :{showtime}')
    except:
        print("message not in database")
        pass
    # gi = pygeoip.GeoIP(GEOIP_DATABASE, pygeoip.GEOIP_STANDARD)
    
    return HttpResponse('<h1>Hello HttpResponse</h1>')

def link(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(f'User IP address : {ip}')
    return HttpResponse("Thank you for sharing your location")