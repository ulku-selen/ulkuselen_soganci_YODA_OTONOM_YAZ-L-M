
class Hesap:
    def __init__(self, sahip_ad, hesap_no, bakiye=0):
        # Hesap sahibinin adı
        self.sahip_ad = sahip_ad
        # Hesap numarası
        self.hesap_no = hesap_no
        # Başlangıç bakiyesi (baslangic 0 olsn)
        self.bakiye = bakiye

    def para_yatir(self, miktar):
        # Para yatırma işlemi
        if miktar > 0:
            self.bakiye += miktar
            print(f"{miktar} TL yatırıldı. Güncel bakiye: {self.bakiye} TL")
        else:
            print("Yatırılacak miktar 0'dan büyük olmalıdır!")

    def para_cek(self, miktar):
        # Para çekme işlemi
        if miktar <= 0:
            print("Çekilecek miktar 0'dan büyük olmalıdır!")
        elif miktar > self.bakiye:
            print("Yetersiz bakiye! İşlem gerçekleştirilemedi.")
        else:
            self.bakiye -= miktar
            print(f"{miktar} TL çekildi. Güncel bakiye: {self.bakiye} TL")

    def bakiye_goster(self):
        print(f"{self.sahip_ad} adlı kişinin güncel bakiyesi: {self.bakiye} TL")


print("Banka Hesap Yönetimi Programına Hoş Geldiniz!")

# Kullanicidan hesap bilgilerini aliyorz
ad = input("Hesap sahibinin adını giriniz: ")
hesap_no = input("Hesap numarasını giriniz: ")

# Baslangıc bakiyesi aliyorz
baslangic = input("Başlangıç bakiyesi (boş bırakırsanız 0 olur): ")

if baslangic == "":
    baslangic = 0
else:
    baslangic = float(baslangic)

# Hesap nesnesi oluşturma
hesap = Hesap(ad, hesap_no, baslangic)

# Menü döngüsü
while True:
    print("\n--- İşlem Menüsü ---")
    print("1 - Para Yatır")
    print("2 - Para Çek")
    print("3 - Bakiye Görüntüle")
    print("4 - Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "1":
        miktar = float(input("Yatırılacak miktar: "))
        hesap.para_yatir(miktar)

    elif secim == "2":
        miktar = float(input("Çekilecek miktar: "))
        hesap.para_cek(miktar)

    elif secim == "3":
        hesap.bakiye_goster()

    elif secim == "4":
        print("Programdan çıkılıyor...")
        break

    else:
        print("Geçersiz seçim! Lütfen tekrar deneyiniz.")
