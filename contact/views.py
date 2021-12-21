from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import FormView, TemplateView
from .forms import ContactForm
from django.urls import reverse_lazy

from django.http import HttpResponse
from PIL import Image
import pytracking
# Create your views here.

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

def clicked(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print("Link clicked")
    print(ip)
    request.session['ip']=ip
    
    return HttpResponse('<h1>Hello HttpResponse</h1>')



def image_load(request):
    print("\nImage Loaded\n")
    red = Image.new('RGB', (1, 1))
    response = HttpResponse(content_type="image/png")
    red.save(response, "PNG")
    return response
