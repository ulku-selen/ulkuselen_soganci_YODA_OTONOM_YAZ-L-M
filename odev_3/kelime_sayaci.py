# kullanicidan metin alcaz
metin = input("Bir metin giriniz: ")

# bosluklar dahil top karakter sayisi
toplam_karakter = len(metin)
kelimeler = metin.split()

# Toplam kelime sayisi
toplam_kelime = len(kelimeler)

#  tüm kelimeleri küçültüyoruz
kelimeler_kucuk = [k.lower() for k in kelimeler]

# En uzun kelimenin uzunluğunu bulma
if kelimeler:
    en_uzun_kelime = max(kelimeler, key=len)
    en_uzun_uzunluk = len(en_uzun_kelime)
else:
    en_uzun_kelime = ""
    en_uzun_uzunluk = 0

# Her kelimenin kaç defa tekrar ettiğini sayiyoz
kelime_sayaci = {}

for kelime in kelimeler_kucuk:
    if kelime in kelime_sayaci:
        kelime_sayaci[kelime] += 1
    else:
        kelime_sayaci[kelime] = 1

print("Toplam kelime sayısı:", toplam_kelime)
print("Toplam karakter sayısı (boşluk dahil):", toplam_karakter)
print("En uzun kelime:", en_uzun_kelime)
print("En uzun kelimenin uzunluğu:", en_uzun_uzunluk)

print("\nKelime tekrar sayıları:")
for kelime, adet in kelime_sayaci.items():
    print(f"'{kelime}' kelimesi {adet} kere geçti.")
