from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomerRegistrationForm, ContactForm
from django.contrib import messages
from .models import *
from datetime import datetime, timedelta
from django.utils import timezone

# Create your views here.
def home(request):
    schedule = Tournament.objects.all().order_by('start_date')[0]
    today = timezone.now()
    two_days_ago = today - timedelta(days=2)
    home_news = News.objects.filter(news_date__range=[two_days_ago, today]).order_by('-news_date')
    return render(request, 'app/index.html', {'home_news': home_news,'schedule': schedule})

def media(request):
    return render(request, 'app/media.html')

def photos(request):
    imgs = GalleryPhoto.objects.all()
    return render(request, 'app/photos.html', {'imgs': imgs})

def videos(request):
    vids = GalleryVideo.objects.all()
    return render(request, 'app/highlights.html', {'vids': vids})

def about(request):
    return render(request, 'app/about.html')

def news(request):
    all_news = News.objects.all()[::-1]
    return render(request, 'app/news.html', {'all_news':all_news})

def schedule(request):
    matches = Tournament.objects.all()
    return render(request, 'app/schedule.html',{'matches':matches})

def profile(request):
    return render(request, 'app/profile.html', )

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, 'Your Message was Sent Succesfully!')
            form = ContactForm()
        return render(request, 'app/contact.html', {'form': form})    
    else:
        form = ContactForm()
        return render(request, 'app/contact.html', {'form': form}) 

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/registration.html', {'form': form})
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registered Sucessfully')
            form.save()
        return render(request, 'app/registration.html', {'form': form})
            


