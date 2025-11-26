print("Basit Hesap Makinesi")
print("İşlemler: +  -  *  /")
while True:  
    islem = input("İşlem seçiniz (+, -, *, / ): ")

    if islem not in ["+", "-", "*", "/"]:
        print("Geçersiz işlem! Tekrar deneyin.")
        continue

    # Kullanıcıdan iki sayı alıyoruz
    sayi1 = float(input("Birinci sayıyı giriniz: "))
    sayi2 = float(input("İkinci sayıyı giriniz: "))

    # Her işlem türüne göre sonuç hesaplama
    if islem == "+":
        sonuc = sayi1 + sayi2
    elif islem == "-":
        sonuc = sayi1 - sayi2
    elif islem == "*":
        sonuc = sayi1 * sayi2
    elif islem == "/":
        # Sıfıra bölme kontrolü
        if sayi2 == 0:
            print("HATA: Bir sayı sıfıra bölünemez!")
            continue
        sonuc = sayi1 / sayi2

    print("Sonuç:", sonuc)
    print("-----------------------------")
