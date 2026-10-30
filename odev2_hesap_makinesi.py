baslikRengi = "\033[31m"
baslikRengiYesil = "\033[32m"
altBaslikRengi = "\033[34m"
SIFIRLA = "\033[0m"

print(f"{baslikRengiYesil}***'Basit hesap makinesi' kullanıyorsun***{SIFIRLA}")

while True:
    


    karar = input("Devam etmek için"f"{baslikRengiYesil}'q' dışında herhangi bir tuşa basın{SIFIRLA}""Çıkış yapmak için"f"{baslikRengi}'q' basın{SIFIRLA}")
    if karar.lower() == "q":
        print("Çıkış yapılıyor...")
        break
        
    try:
        a = float(input("1 numaralı sayıyı girin: "))
        b = float(input("2 numaralı sayıyı girin: "))
    except ValueError:
        print("hatalı sayı girişi yaptınız. "f"{altBaslikRengi}Başa dönülüyor...{SIFIRLA}")
        continue

    islem = input("bir işlem türü seçin(+,-,*,/,**,//)(UYARI! Lütfen % işareti girmeyin): ")


    if islem == "+":
        print(a+b)
    elif islem == "-":
        print(a-b)
    elif islem == "*":
        print(a*b)
    elif islem == "/":
        if b !=0:
            print(a/b)
        else:
            print("sayıyı sıfıra bölemiyorum")
    elif islem == "**":
        print(a**b)
    elif islem == "%":
        print(f"{altBaslikRengi}Lütfen demiştim :) {SIFIRLA}")
    elif islem == "//":
        if b != 0:
            print(a//b)
        else:
            print("sayıyı sıfıra bölemiyorum")
    else:
        print("hatalı operatör yada sayı girdin")
    
    


    
    
    
    