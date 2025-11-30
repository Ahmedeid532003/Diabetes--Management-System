from django.urls import path
from . import views
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_page, name='login_page'),
    path('login_user/', views.login_user, name='login_user'),
    path('info/', views.info, name='info'),
    path('DAT/', views.DAT, name='DAT'),
    path('', views.home_page, name='home_page'),
    path('ex/', views.ex, name='ex'),
    path('in/', views.inn, name='in'),
    path('inside/', views.inside, name='inside'),
    path('second_page/', views.second_page, name='second_page'),
    path('SECOND__PAGE/', views.SECOND__PAGE, name='SECOND__PAGE'),
    path('EnterDataYourself/', views.EnterDataYourself, name='EnterDataYourself'),
    path('Data/', views.Data, name='Data'),
    path('Survey/', views.Survey, name='Survey'),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)