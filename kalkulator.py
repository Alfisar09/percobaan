print("Kalkulator")
a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
pilihan = input("Pilih operasi (+, -, *, /, %): ")
if pilihan == "*":
    print(f'hasil dari {a} dan {b} adalah {a * b}')
elif pilihan == "/":
    print(f'hasil dari {a} dan {b} adalah {a / b}')
elif pilihan == "%":
    print(f'hasil dari {a} dan {b} adalah {a % b}')
elif pilihan == "-":
    print(f'hasil dari {a} dan {b} adalah {a - b}')
elif pilihan == "+":
    print(f'hasil dari {a} dan {b} adalah {a + b}')
else: print("coba lagi")