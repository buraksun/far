from django import forms


class Form(forms.Form):
    ad = forms.CharField(required=True , label="Ad ve Soyad", widget= forms.TextInput(attrs={'placeholder':'Adınız Soyadınızı Giriniz'}))
    mail = forms.EmailField(required=True , widget= forms.TextInput(attrs={'placeholder':'Mail Adresinizi Giriniz'}))
    telefon = forms.CharField(required=True , min_length=7 , max_length=12 , widget= forms.TextInput(attrs={'placeholder':'Telefon Numaranızı Giriniz'}))
    aciklama = forms.CharField(label="Açıklama" , widget=forms.Textarea(attrs={'placeholder':'Açıklama Giriniz'}))


siparis =( 
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),

) 

class Siparis(forms.Form):
    ad = forms.CharField(required=True , widget= forms.TextInput(attrs={'placeholder':'Adınız Soyadınız'}))
    mail = forms.EmailField(required=True , widget= forms.TextInput(attrs={'placeholder':'Mail Adresinizi Giriniz'}))
    telefon = forms.CharField(required=True , max_length=12 , widget= forms.TextInput(attrs={'placeholder':'Telefon Numaranızı Giriniz'}))
    erkek_kuzu = forms.ChoiceField(required=True , choices = siparis , label="Sipariş Edilecek Erkek Kuzu Sayısı" )
    disi_kuzu = forms.ChoiceField(required=True , choices = siparis , label="Sipariş Edilecek Dişi Kuzu Sayısı")




