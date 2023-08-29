from django.urls import path
from six_a_side import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm
urlpatterns = [

    path('', views.home, name='home' ),
    path('media/', views.media, name='media' ),
    path('photos/', views.photos, name='photos' ),
    path('videos/', views.videos, name='videos' ),
    path('about/', views.about, name='about' ),
    path('news/', views.news, name='news' ),
    path('schedule/', views.schedule, name='schedule' ),
    path('contact/', views.contact, name='contact' ),

    path('accounts/login/', auth_views.LoginView.as_view(template_name = 'app/login.html', authentication_form = LoginForm), name = 'login'),
    path('profile/', views.profile, name='profile' ),
    path('registration/', views.CustomerRegistrationView.as_view(), name = 'registration'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)