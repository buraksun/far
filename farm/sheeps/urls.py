from django.contrib import admin
from django.urls import path , include
from .views import index , hakkimizda , galeri , turlermiz , siparis , iletisim 

urlpatterns = [
    path('', index , name="index"),
    path('hakkimizda', hakkimizda , name="hakkimizda"),
    path('galeri', galeri , name="galeri"),
    path('turlermiz', turlermiz , name="turlerimiz"),
    path('siparis', siparis , name="siparis"),
    path('iletisim', iletisim , name="iletisim"),

]
