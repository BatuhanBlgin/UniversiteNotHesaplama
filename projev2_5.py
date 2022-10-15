# =========================================#
# Gerekli Kütüphaneleri Ekliyoruz
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk

# =========================================#

class hesaplama():
    # =========================================#
    def __init__(self):
        self.toplamnot = 0
        self.toplamkredi = 0
        self.derssayisi = 0

        # =========================================#
        # Arkaplan Eklemek İçin Gerekli Kodlar
        self.foto = ImageTk.PhotoImage(file="arkaplan.png")
        self.fotograf = tk.Label(image=self.foto)
        self.fotograf.pack()
        # =========================================#
        # Bilgi Yazıları Oluşturmak İçin Kodlar
        self.l1 = tk.Label(text="Ders Adı", font="Arial 13 bold")
        self.l1.place(x=38, y=110)
        self.l2 = tk.Label(text="Ders Kredisi", font="Arial 13 bold")
        self.l2.place(x=368, y=110)
        self.l3 = tk.Label(text="Harf Notu", font="Arial 13 bold")
        self.l3.place(x=528, y=110)
        self.l4 = tk.Label(text="Ders Adları", font="Arial 13 bold")
        self.l4.place(x=38, y=170)
        self.l5 = tk.Label(text="Ders Kredileri", font="Arial 13 bold")
        self.l5.place(x=368, y=170)
        self.l6 = tk.Label(text="Harf Notları", font="Arial 13 bold")
        self.l6.place(x=528, y=170)
        self.dersbilgi = tk.Label(text="Toplam Ders Sayısı: 0 ", font="Arial 12 bold")
        self.dersbilgi.place(x=150, y=710)
        self.notbilgi = tk.Label(text="Girilen Toplam Not: 0 ", font="Arial 12 bold")
        self.notbilgi.place(x=151, y=733)
        self.kredibilgi = tk.Label(text="Girilen Toplam Kredi: 0 ", font="Arial 12 bold")
        self.kredibilgi.place(x=350, y=733)
        self.donemnotu = tk.Label(text="Dönem Sonu Notunuz: 0 ", font="Arial 12 bold")
        self.donemnotu.place(x=350, y=710)
        self.harfbilgi = tk.Label(text="Harf Notları: AA, BA, BB, CB, CC, DC, DD, FD, FF", font="Arial 12 bold")
        self.harfbilgi.place(x=155, y=760)
        self.baslik = tk.Label(text="Zımba Python Ekibi\nÜniversite Yıl Sonu Not Hesaplama Aracı",
                               font="Arial 16 bold")
        self.baslik.place(x=140, y=20)

        # =========================================#
        # Ders Adı Kredi Ve Harf Notu Girişlerini Oluşturmak İçin Kullanılan Kodlar
        self.Dersentry = tk.Entry(width=33, font="Arial 12 bold")
        self.Dersentry.place(x=40, y=140)
        self.Kredientry = tk.Entry(width=14, font="Arial 12 bold")
        self.Kredientry.place(x=370, y=140)
        self.Harfentry = tk.Entry(width=14, font="Arial 12 bold")
        self.Harfentry.place(x=530, y=140)
        # =========================================#
        # Ders Adlarının Ders Kredilerinin Ve Harf Notlarının Bir Araya Toplandığı List Boxları Oluşturmak İçin Kullanılan Kodlar

        self.dersadlari = tk.Listbox(width=42, height=25, font="Arial 10 bold")
        self.dersadlari.place(x=40, y=200)
        self.dersakredileri = tk.Listbox(width=18, height=25, font="Arial 10 bold")
        self.dersakredileri.place(x=370, y=200)
        self.harfnotlari = tk.Listbox(width=18, height=25, font="Arial 10 bold")
        self.harfnotlari.place(x=530, y=200)
        # =========================================#
        # Butonları Oluşturmak İçin Kullanılan Kodlar
        # text=Buton Üzerindeki Yazı,Widht=Buton Genişliği,Height=Buton Yüksekliği,bg=Buton Rengi,fg=Yazı Rengi,
        # activebackground=Basıldığı Zaman Butonun Rengi,activeforeground=Basıldıgı Zaman Yazı Rengi,Font=Yazının Fontu Ve Boyutu,
        # command=Butona Tıklandıgında Ne Yapıcagını Belirler
        self.Eklebuton = tk.Button(text="EKLE", width=8, height=2, bg="green3", fg="White",
                                   activebackground="Green",
                                   activeforeground="white", font="Arial 13 bold", command=self.ekle)
        self.Eklebuton.place(x=55, y=650)
        self.Hesaplabuton = tk.Button(text="HESAPLA", width=8, height=2, bg="Green3", fg="White",
                                      activebackground="Green",
                                      activeforeground="white", font="Arial 13 bold", command=self.hesapla)
        self.Hesaplabuton.place(x=155, y=650)
        self.secimsil = tk.Button(text="SEÇİM SİL", width=8, height=2, bg="Red2", fg="White",
                                  activebackground="Red4",
                                  activeforeground="white", font="Arial 13 bold", command=self.secimsil)
        self.secimsil.place(x=255, y=650)
        self.Temizlebuton = tk.Button(text="TEMİZLE", width=8, height=2, bg="Red2", fg="White",
                                      activebackground="Red4",
                                      activeforeground="white", font="Arial 13 bold", command=self.temizle)
        self.Temizlebuton.place(x=355, y=650)
        self.düzenle = tk.Button(text="DÜZENLE", width=8, height=2, bg="Red2", fg="White",
                                 activebackground="Red4",
                                 activeforeground="white", font="Arial 13 bold", command=self.düzenleme)
        self.düzenle.place(x=455, y=650)
        self.kaydet = tk.Button(text="KAYDET", width=8, height=2, bg="Red2", fg="White",
                                activebackground="Red4",
                                activeforeground="white", font="Arial 13 bold", command=self.kaydet)
        self.kaydet.place(x=555, y=650)

    # =========================================#
    def ekle(self):
        self.hata()  #Hata fonksiyonunu çağırır
        if self.hatadurum == False:  # Hata durumu false gelirse işlemleri yapar
            try:
                self.b = self.harfnotu(str(self.Harfentry.get()).upper())  #harf entry den girilen harf notu
                # değerini harfnotu fonksiyonuna gönderip sayı olarak karşılık değerini alır ve b ye eşitler
                self.a = int(self.Kredientry.get()) #kredi entry den gelen değeri a ya eşitler
                self.toplamnot += self.b * self.a  # toplam notu bulmak için b değerini ve a değerini çarpar
                self.toplamkredi += self.a # a değerini toplam krediye ekler
                self.derssayisi += 1 # ders sayisini bir arttırır
                # =========================================#
                #Ders adı ders kredisi ve ders harf notunu listboxlara ekler
                self.dersadlari.insert("0", self.Dersentry.get())
                self.dersakredileri.insert("0", self.Kredientry.get())
                self.harfnotlari.insert("0", str(self.Harfentry.get()).upper())
                # =========================================#
                # Entrylerdeki Veriler Temizlenir
                self.Kredientry.delete(0, 'end')
                self.Dersentry.delete(0, 'end')
                self.Harfentry.delete(0, 'end')
                # =========================================#
            except:
                pass
   # =========================================#

    # =========================================#
    def hata(self):
        self.hatadurum = False # Hata Durumu False Olarak Başlatılır
        self.harfnotlari1 = ["AA", "BA", "BB", "CB", "CC", "DC", "DD", "FD",
                             "FF"]  # Entry Den Gelen Harf Notunu Kontrol Etmek İçin Liste
        #if komutunun görevi entrylerdeki verileri alıp len ile girilen değer uzunluğunu kontrol etmektir
        #Eğer herhangi bir entry den gelen değer 0 ise uyarı verir hatadurumunu true yapar
        if len(self.Kredientry.get()) == 0 or len(self.Dersentry.get()) == 0 or len(self.Harfentry.get()) == 0:
            messagebox.showinfo("Hata", "Lütfen Boş Alan Bırakmayınız")
            self.hatadurum = True


        #Elif komutunun görevi entrylerden gelen değerlerin str olup olmadığına bakar sonrasında
        #Gelen harf notu değeri listenin içinde yoksa uyarı verir sonrasında kredi entryden gelen değeri
        #int değerine çevirmeye çalışır eğer yapamaz ise hata verir
        elif type(self.Harfentry.get()) == str or (type(self.Kredientry.get()) == str):

            if str(self.Harfentry.get()).upper() not in self.harfnotlari1:
                messagebox.showinfo("Hata", "Lütfen Geçerli Bir Harf Notu Giriniz")

            try:
                int(self.Kredientry.get())
            except:
                messagebox.showinfo("Hata", "Lütfen Ders Kredisine Sadece Rakam Giriniz")
        else:
            pass
    # =========================================#

    # =========================================#
    def hesapla(self):
        #hesaplama fonksiyonu güncelleme seçim sil ve diğer fonksiyonlardan sonra çalıştığı için
        #Eğer ders sayisi 0 a düşerse bilgileri 0 ile güncellemek için kullanılan bir if barındırıyor
        if self.derssayisi == 0:
            self.dersbilgi['text'] = "Toplam Ders Sayısı: 0"
            self.notbilgi['text'] = "Girilen Toplam Not: 0"
            self.kredibilgi['text'] = "Girilen Toplam Kredi: 0"
            self.donemnotu['text'] = "Dönem Sonu Notunuz: 0"

        try:
            #Dönem sonu notu sonucuna ulaşılmak için toplam not ve toplam kredi bölünür
            self.sonuc = (self.toplamnot / self.toplamkredi)
            #Sonrasında bilgi yazılarına bütün değerler yazdırılır
            self.dersbilgi['text'] = "Toplam Ders Sayısı: {}".format(self.derssayisi)
            self.notbilgi['text'] = "Girilen Toplam Not: {}".format(self.toplamnot)
            self.kredibilgi['text'] = "Girilen Toplam Kredi: {}".format(self.toplamkredi)
            #Dönem sonu notu yazdırılırken round ile yuvarlama yapılır
            self.donemnotu['text'] = "Dönem Sonu Notunuz: {}".format(round(self.sonuc, 2))
        except:
            pass

    # =========================================#
    def temizle(self):
        #Bütün Her şeyi Temziler
        self.derssayisi = 0
        self.toplamnot = 0
        self.toplamkredi = 0
        self.sonuc = 0
        self.Kredientry.delete(0, 'end')
        self.Dersentry.delete(0, 'end')
        self.Harfentry.delete(0, 'end')
        self.dersadlari.delete(0, 'end')
        self.dersakredileri.delete(0, 'end')
        self.harfnotlari.delete(0, 'end')
        self.dersbilgi['text'] = "Toplam Ders Sayısı: {}".format(self.derssayisi)
        self.kredibilgi['text'] = "Girilen Toplam Kredi: {}".format(self.toplamkredi)
        self.notbilgi['text'] = "Girilen Toplam Not: {}".format(self.toplamnot)
        self.donemnotu['text'] = "Dönem Sonu Notunuz: {}".format(self.sonuc)
    # =========================================#
    def secimsil(self):
        try:
            try:
                #194. satırdan 201. satıra kadar uzanan kodların amacı şudur
                self.sil = self.dersadlari.curselection() #Ders Adı seçilir ve seçim sil dendiği an değer
                #curselection komutu ile görülür fakat seçilen değer 0. değer için (0,) şeklinde gelir
                #bilgisyara bu değeri int değeri olarak göstermemiz lazım ki dersi ordan silebilelim
                #bunun için şöyle bir şey düşündük
                #gelen değeri str yapıp  sonrasında içersinde dolaşıp sayı değerini alalım sonrasında int yapıp işlemlerimizi yapalım
                #fakat şöyle bir sorunla karşılaştık [1:2] oldugu zaman 0 dan 9 a kadar olan dersleri silebiliyordu ama 10. ders ve üstü seçildiği zaman
                #örnek olarak (10,) diye  gelen değeri 1 olarak görüyordu ve 1. dersi listeden siliyordu bizde bu sebepten dolayı try komutundan faydalandık ve
                #şöyle bir işlem kurduk gelen değeri ilk önce [1:3] olarak alıyoruz ve int yapmaya çalışıyoruz değer 0 veya 9 arasında ise 1:3 oldugunda
                # 0,- 1, - 2, vb  geliceği için int yapamıyordu sonrasında bunu [1:2] olarak yapmaya çalıştığında sayıya ulaşıp inte dönüştürüp işlem yapabilir hale
                #geldi yani değer (10,) ve üstü  olarak gelirse [1:3] çalışıyor (9,) ve altı gelirse [1:2] çalışıyor
                self.sil = str(self.sil)[1:3]
                self.sil = int(self.sil)

            except:
                self.sil = self.dersadlari.curselection()
                self.sil = str(self.sil)[1:2]
                self.sil = int(self.sil)

            secimsoru = tk.messagebox.askquestion("Ders Silinecek",
                                                  "{} Adlı Dersi Listeden Silmek İstediğinize Emin misiniz?".format( self.dersadlari.get(self.sil)),icon="warning")
                                                   # kişiye dersi silip silmek istemediiği son kez soruluyor
            if secimsoru == 'yes':  #eğer kişi evet derse silme işlemlerini yapıyor
                self.derssayisi -= 1 # ders sayısını 1 eksiltiyor
                self.a = int(self.dersakredileri.get(self.sil)) #liste içersinden sil den gelen sayı kaç ise o değeri alıyor ve a ya eşitliyor
                self.b = self.harfnotu(str(self.harfnotlari.get(self.sil))) #liste içersinden sil den gelen sayı kaç ise o değeri alıyor ve harf notuna str olarak
                # yolladıktan sorna gelen değeri b ye eşitliyor
                self.toplamkredi -= self.a # toplam krediden a  değerini çıkartıyor
                self.toplamnot -= self.a * self.b # toplam nottan a ile b değerini çarpıp çıkartıyor
                self.dersadlari.delete(self.sil) # ders adlarinin bulundugu selectbox dan kaçıncı sayı geldiyse onu siliyor
                self.dersakredileri.delete(self.sil) #  ders kredilerinin bulundugu selectbox dan kaçıncı sayı geldiyse onu siliyor
                self.harfnotlari.delete(self.sil) #  ders harfnotlarının bulundugu selectbox dan kaçıncı sayı geldiyse onu siliyor
                self.hesapla() #hesapla fonksiyonu çalıştırılıyor
        except:
            pass

    # =========================================#
    def düzenleme(self):
        durum2 = False #durum2 değeri false olarak belirleniyor
        try:
            try: #seçimsilde yapılan işlemler tekrar yapılıyor
                 #fakat bu sefer koşul sağlanırsa  durum2 True değerine çevriliyor
                 # sebebi eğer ders seçilmediyse 249. satırda bulunana if değeri çalışmıyor ve güncelleme penceresini getirmiyor
                self.düzenle = self.dersadlari.curselection()
                self.düzenle = str(self.düzenle)[1:3]
                self.düzenle = int(self.düzenle)
                durum2 = True
            except:
                self.düzenle = self.dersadlari.curselection()
                self.düzenle = str(self.düzenle)[1:2]
                self.düzenle = int(self.düzenle)
                durum2 = True
        except:
            pass
        try:
            if durum2 == True:
                self.düzen = tk.Tk()
                self.düzen.iconbitmap('icon.ico')
                self.düzen.title("Yeni Değerleri Giriniz")
                self.düzen.geometry("215x220+950+300")
                self.düzen.resizable(False, False)
                self.adlabel = tk.Label(self.düzen, text="Ders Adı", font="Arial 12 bold")
                self.adlabel.pack()
                self.addüzen = tk.Entry(self.düzen, width=14, font="Arial 12 bold")
                self.addüzen.insert(0, str(self.dersadlari.get(str(self.düzenle))))
                self.addüzen.pack()
                self.kredilabel = tk.Label(self.düzen, text="Ders Kredisi", font="Arial 12 bold")
                self.kredilabel.pack()
                self.kredidüzen = tk.Entry(self.düzen, width=14, font="Arial 12 bold")
                self.kredidüzen.insert(0, str(self.dersakredileri.get(str(self.düzenle))))
                self.kredidüzen.pack()
                self.harflabel = tk.Label(self.düzen, text="Harf Notu", font="Arial 12 bold")
                self.harflabel.pack()
                self.harfdüzen = tk.Entry(self.düzen, width=14, font="Arial 12 bold")
                self.harfdüzen.insert(0, str(self.harfnotlari.get(str(self.düzenle))))
                self.harfdüzen.pack()

                self.güncellebuton = tk.Button(self.düzen, text="Güncelle", command=self.güncelle, width=10, height=2,
                                               bg="Green2", fg="White", activebackground="Red4",
                                               activeforeground="white", font="Arial 15 bold", )
                self.güncellebuton.pack()



        except:
            pass

    # =========================================#
    def güncelle(self):
        #düzenle def i içersinde oluşturulan tkinter penceresindeki güncelle butonuna tıklandığı zaman bu fonksiyon çalışır ve
        # ilk başta ekle fonksiyonunda olduğu gibi hata ayıklama işlemleri yapılır hata fonksiyonu çağırılmaz çünki değerler
        #kontrol farklı entryler için yapılır
        durum = False
        if len(self.addüzen.get()) == 0 or len(self.kredidüzen.get()) == 0 or len(self.harfdüzen.get()) == 0:
            messagebox.showinfo("Hata", "Lütfen Boş Alan Bırakmayınız")
            durum = True

        elif type(self.harfdüzen.get()) == str or (type(self.kredidüzen.get()) == str):
            if str(self.harfdüzen.get()).upper() not in self.harfnotlari1:
                messagebox.showinfo("Hata", "Lütfen Geçerli Bir Harf Notu Giriniz")
                durum = True
            try:
                self.a = int(self.kredidüzen.get())
            except:
                messagebox.showinfo("Hata", "Lütfen Ders Kredisine Sadece Rakam Giriniz")
                durum = True
        else:
            pass

        if durum == False:
            #Eğer durum değeri değişmemiş ve false gelirse işlemler tekrar düzenleden gelen ders için yapılır

            try:
                # ilk başta seçilen dersin değerleri temizlenir
                self.a = int(self.dersakredileri.get(self.düzenle))
                self.b = self.harfnotu(str(self.harfnotlari.get(self.düzenle)))
                self.toplamnot -= self.b * self.a
                self.toplamkredi -= self.a
                self.dersadlari.delete(self.düzenle)
                self.dersakredileri.delete(self.düzenle)
                self.harfnotlari.delete(self.düzenle)
                # sonrasında yeni girilen değerler ile tekrar eklenir
                self.b = self.harfnotu(str(self.harfdüzen.get()).upper())
                self.a = int(self.kredidüzen.get())
                self.toplamnot += self.b * self.a
                self.toplamkredi += self.a
                self.dersadlari.insert("0", self.addüzen.get())
                self.dersakredileri.insert("0", str(self.kredidüzen.get()))
                self.harfnotlari.insert("0", str(self.harfdüzen.get()).upper())
                self.hesapla() # hesapla fonksiyonu çağırılır
                self.düzen.destroy() # açılan güncelleme penceresi kapanır
            except:
                pass
        else:
            self.düzen.destroy()

    # =========================================#
    def kaydet(self):
        #kaydet butonuna tıklandıgında eger ders sayisi 1 veya fazlasıysa çalışır
        if self.derssayisi >= 1:
            #Kayıt yaparken program sizden adınızı soyadınızı ve okuduğunuz bölüm bilgisini ister bu veriler sadece txt dosyasında yer alır
            #harici biryere kayıt edilmez
            #ad soyad girilmesi için gerekli entryler tkinter penceresinde oluşturulur
            self.kayit = tk.Tk()
            self.kayit.geometry("240x170")
            self.kayit.title("zimba takimi")
            self.isimbilgi = tk.Label(self.kayit, text="Adınız Soyadınız *", font="Arial 13 bold")
            self.isimbilgi.pack()
            self.isimentry = tk.Entry(self.kayit, font="Arial 15 bold")
            self.isimentry.pack()
            self.bölümbilgi = tk.Label(self.kayit, text="Okuduğunuz Bölüm *", font="Arial 13 bold")
            self.bölümbilgi.pack()
            self.bölümentry = tk.Entry(self.kayit, font="Arial 15 bold")
            self.bölümentry.pack()
            self.bilgial = tk.Button(self.kayit, width=20, height=2, text="Kaydet", command=self.tamkayıt, bg="Green2",
                                     fg="White", activebackground="Red4",
                                     activeforeground="white", font="Arial 15 bold")  # butona basıldıgında tamkayıt fonksiyonun çalıştırır
            self.bilgial.place(x=0, y=110)
            print()
        else:
            messagebox.showinfo("Hata", "Kayıt İşlemi Yapmadan Önce Lütfen Ders Giriniz")  # eger gerekli if koşulu sağlanmaz ise hata verir

    def tamkayıt(self):
        # tam kayıt fonksiyonu çalıştıgı an isim ve bölüm entrysine girilen veriler alınır
        self.isimentry = str(self.isimentry.get()).upper()
        self.bölümentry = str(self.bölümentry.get()).upper()

        if len(self.isimentry) != 0 and len(self.bölümentry) != 0:  #ve boş bırakılmış mı diye ufak bir kontrole girer

            try:
                self.kayit.destroy() # kayıt penceresi kapatılır
                self.kayityer = filedialog.askdirectory() + "/" # kişiden kayıt yer seçmesi istenir
                self.listders = list(self.dersadlari.get(0, 'end')) # ders adları liste olarak alınır
                self.listkredi = list(self.dersakredileri.get(0, 'end')) # ders kredileri liste olarak alınır
                self.listharf = list(self.harfnotlari.get(0, 'end')) # ders harf notları liste olarak alınır
                kayıt = open(self.kayityer + "sonuc.txt", "w") #secilen kayıt yeri bilgisine sonuc.txt ekleyerek txt dosyası "w" modunda oluşturulur
                kayıt.write("Ad Soyad:" + self.isimentry + "\n" + "Bölüm:" + self.bölümentry + "\n") #txt dosyasına ad soyad ve bölüm bilgisi yazdırılır
                kayıt.write("-" * 50 + "\n") # verilerin daha anlaşılır olması için 50 adet - koyulur
                kayıt.write("Sonuç:" + "\n") # sonuç kısmı için başlık atılır
                self.hesapla() # son kez bütün bilgilerin doğrulugu kontrol edilmek için hesapla fonksiyonu çalıştırılır
                kayıt.write(
                    "Toplam Ders Sayisi" + " " + str(self.derssayisi) + "\n" + "Girilen Toplam Kredi" + " " + str(
                        self.toplamkredi) + "\n" + "Girilen Toplam Not" + " " + str(
                        self.toplamnot) + "\n" + "Donem Sonu Notunuz" + " " + (str(self.sonuc)[0:4]) + "\n") #ders sayisi,toplam kredi,toplam not ve sonuç txt dosyasına
                #düzenli bir şekilde yazdırılır
                kayıt.write("-" * 50 + "\n")  # verilerin daha anlaşılır olması için 50 adet - koyulur

                kayıt.write("Ders Adi" + " " + "Ders Kredisi" + " " + "Harf Notu" + "\n")  #verilerin txt ye yazılma sırasını belirten ufak bir bilgi yazısı yazılır
                kayıt.write("Dersler:" + "\n") # dersleri belirten bir başlık atılır

                for i in range(len(self.listders)):   #listders yani toplam ders uzunlugunu alan bu kod sayesinde for döngüsündeki i yi ders sayısı
                    #kadar döndürebiliyoruz
                    kayıt.write("-" * 50 + "\n") # düzenli olsun diye her ders arasına 50 adet - koyulur
                    kayıt.write(
                        str(self.listders[i] + " " * 5 + str(self.listkredi[i]) + " " * 5 + str(
                            self.listharf[i]) + "\n"))  # for döndükce i değeri kaça eşit ise o veri çekilir ve sırasıyla yazdırılır

                kayıt.close() # dosya kapatılır
                messagebox.showinfo("Başarılı",
                                    "Kayıt İşlemi Başarıyla Seçtiğiniz {} Hedefine 'sonuc.txt' Dosya ismiyle Başarıyla Kayıt Edilmiştir"
                                    .format(self.kayityer)) #ardından kişi dosyanın nereye kayıt edilmesini istediyse kayıt yerinin yolu ve dosyanın adını kişiye
                                    #kayıt işlemi başarılı şeklinde bi bilgilendirme penceresi gösterir
            except:
                pass
        else:
            messagebox.showinfo("Hata", "Lütfen Gerekli Alanları Doldurunuz") # eğer boş bırakılırsa hata verir
            self.kayit.destroy()


    def harfnotu(self, x):
        #harf notlarının str olarak yollandıgı ve geri int değeri döndüren harfnotu def i içersinde harf notlarını barındıran bir sözlük yer alıyor
        self.notlar = {"AA": 4.0, "BA": 3.5, "BB": 3.0, "CB": 2.5, "CC": 2.0, "DC": 1.5, "DD": 1.0, "FD": 0.5,
                       "FF": 0}
        if x == "AA":
            return self.notlar.get("AA")
        elif x == "BA":
            return self.notlar.get("BA")
        elif x == "BB":
            return self.notlar.get("BB")
        elif x == "CB":
            return self.notlar.get("CB")
        elif x == "CC":
            return self.notlar.get("CC")
        elif x == "DC":
            return self.notlar.get("DC")
        elif x == "DD":
            return self.notlar.get("DD")
        elif x == "FD":
            return self.notlar.get("FD")
        elif x == "FF":
            return self.notlar.get("FF")


pencere = tk.Tk()
pencere.title("ZIMBA EKİBİ V2.5") #zımba ekibi v2.5 hazır bundan önceki sürümleri beğenmediğimiz , eksikleri ve hataları olduğu için v2.5 ile karşınızdayız :)
pencere.resizable(False, False)
pencere.geometry("700x800+700+100")
pencere.iconbitmap('icon.ico')
hesaplama()
pencere.mainloop()
