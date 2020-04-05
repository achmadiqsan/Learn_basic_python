print"----PERHITUNGAN DATA----"
print
X = (raw_input('Masukkan Angka Pertama : '))
Y = (raw_input('Masukkan Angka Kedua : '))
A1 = float(X)
A2 = float(Y)
HT = A1 + A2
HK = A1 - A2
HKL = A1 * A2
HB = A1 / A2
RT = (A1 + A2)/2
print
print"----HASIL PEERHITUNGAN----"
print("Hasil Penjumlahan : "+ format(HT,'.2f'))
print("Hasil Pengurangan : "+ format(HK,'.2f'))
print("Hasil Perkalian : "+ format(HKL,'.2f'))
print("Hasil Pembagian : "+ format(HB,'.2f'))
print("NIlai Rata-rata : "+ format(RT,'.2f'))
print"============================================"
raw_input()
