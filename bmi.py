print("Body Mass Index Calculator")
a = float(input("Masukkan berat badan (kg): "))
b = float(input("Masukkan tinggi badan (m): "))
kalkulasi = a / (b**2)
if kalkulasi < 18.5:
    print("Berat badan anda kurang, anda termasuk kategori kurang")
elif kalkulasi >= 18.5 and kalkulasi <= 24.9:
    print("Berat badan anda ideal, anda termasuk kategori normal")
elif kalkulasi >= 25 and kalkulasi <= 29.9:
    print("Berat badan anda berlebihan, anda termasuk kategori berat")
else:
    print("Berat badan anda sangat berlebihan, anda termasuk kategori obesitas")

