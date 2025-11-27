import random  #rastgele sayi uretmek icin

print("1 ile 100 arasında bir sayı tuttum. 10 tahmin hakkınız var.")

hedef = random.randint(1, 100)  # 1-100 arasi rastgele sayi sec
hak = 10                       # Toplam tahmin hakki
deneme = 0                     # deneme sayisi

while hak > 0:
    tahmin = int(input("Tahmininizi giriniz: "))
    deneme += 1     # Deneme sayisi artar
    hak -= 1        # Hak azalir

    if tahmin == hedef:
        print(f"Tebrikler! {deneme}. denemede doğru bildiniz!")
        break
    elif tahmin < hedef:
        print("Daha büyük bir sayı giriniz.")
    else:
        print("Daha küçük bir sayı giriniz.")

    print(f"Kalan tahmin hakkı: {hak}")

# hak biterse 
if hak == 0 and tahmin != hedef:
    print("Tahmin hakkınız bitti, oyunu kaybettiniz.")
    print("Tuttuğum sayı:", hedef)
