print(f"{'| ASCII KODU':^10}",f"{'| KARAKTER':^20}")
print("-"*30)
for i in range(0,128):
    if i < 32 or i==127:
        print(f"| {i:<10}    | [kontrol karakteri]")
    elif i==32:
        print(f"| {i:<10}    | [boşluk]")
    else:
        print(f"| {i:<10}    |", chr(i))
    