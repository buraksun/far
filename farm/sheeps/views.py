from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.urls import reverse
from .forms import Form , Siparis

def index(request):
    return render(request , 'index.html')

def hakkimizda(request):
    return render(request , 'about.html')

def galeri(request):
    return render(request , 'gallery.html')

def turlermiz(request):
    return render(request , 'icons.html')

def iletisim(request):
    if request.method == 'GET':
        form = Form()
    else:
        form = Form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['ad']
            from_email = form.cleaned_data['mail']
            subject = form.cleaned_data['telefon']
            message = form.cleaned_data['aciklama']
            icerik = f'Ad ve Soyad : {name}\nMail Adresi : {from_email}\nTelefon Numarası : {subject}\nMesaj : {message}'
            send_mail('Yeni Bir Müşteriniz Var', icerik , {from_email}, ['tunahan.ucer@hotmail.com'] , fail_silently=False)
            return redirect('iletisim')
    return render(request, "mail.html", {'form': form})


def siparis(request):
        if request.method == 'GET':
            form  = Siparis()

        else:
            if request.method == 'POST':
                if 'gonder' in request.POST:
                    name = request.POST['ad']
                    mail = request.POST['mail']
                    telefon = request.POST['telefon']   
                    disi_kuzu = request.POST['disi_kuzu']   
                    erkek_kuzu = request.POST['erkek_kuzu']  
                   
                    form = Siparis(request.POST)
                    if form.is_valid():
                        toplam = (int(erkek_kuzu)*3500)+(int(disi_kuzu)*3000)
                        rezervasyon = toplam*8/100
                        toplam_siparis = toplam - rezervasyon
                        hesaba_yatırılacak = (toplam_siparis*25)/100
                        return render(request , 'siparis.html' , {'form' : form , 'name':name , 'erkek_kuzu': erkek_kuzu , 'disi_kuzu':disi_kuzu , 'toplam' : toplam , 'rezervasyon' : rezervasyon , 'toplam_siparis' : toplam_siparis , 'hesaba_yatırılacak' : hesaba_yatırılacak})
                
                if 'evet' in request.POST:
                    name = request.POST['ad']
                    mail = request.POST['mail']
                    telefon = request.POST['telefon']   
                    disi_kuzu = request.POST['disi_kuzu']   
                    erkek_kuzu = request.POST['erkek_kuzu']  
                   
                    form = Siparis(request.POST)
                    if form.is_valid():
                        toplam = (int(erkek_kuzu)*3500)+(int(disi_kuzu)*3000)
                        rezervasyon = toplam*8/100
                        toplam_siparis = toplam - rezervasyon
                        hesaba_yatırılacak = (toplam_siparis*25)/100
                        icerik = f'Ad ve Soyad : {name}\nMail Adresi : {mail}\nTelefon Numarası : {telefon}\nDişi Kuzu Sayısı : {disi_kuzu}\nErkek Kuzu Sayısı : {erkek_kuzu}\nToplam Tutar : {toplam} ₺\nErken Rezervasyon İndirimi : {rezervasyon} ₺\nToplam Sipariş Tutarı : {toplam_siparis} ₺\nErken Rezervasyon İçin Hesaba Yatırılması Gereken Tutar : {hesaba_yatırılacak} ₺'
                        send_mail('Yeni Bir Siparişiniz Var', icerik , 'tunahan.ucer@hotmail.com' , ['tunahan.ucer@hotmail.com'] , fail_silently=False)
                        return(redirect('siparis'))                    

        return(render(request , 'siparis.html' , {'form':form}))
