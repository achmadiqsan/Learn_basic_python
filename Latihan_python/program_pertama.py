'''
#program menampilkan teks pada python
print 'selamat datang di dunia python programming'
print '=========================================='
print 
print 'ini program pertama ku pada python'
print 'by near'
'''
'''
print('----masukkan data pribadi anda----')
print
nama = (raw_input('nama lengkap anda : '))
pekerjaan = (raw_input('pekerjaan : '))
umur = int(raw_input('umur : '))
alamat = raw_input('alamat lengkap : ')
print
print('----keterangan data pribadi anda----')
print"nama lengkap anda adalah : ",nama
print"pekerjaan anda adalah : ", pekerjaan
print"umur anda adalah : ", (str(umur)) + " tahun"
print"alamat anda adalah : ",alamat
'''

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
print("NIlai Rata-rata : "+ format(RT,'.2f')

'''
print"----------NILAI MAHASISWA----------"
print"+++++++++++++++++++++++++++++++++++"
print
NS = (raw_input('Masukkan NO.Stambuk : '))
NM = (raw_input('Masukkan Nama       : '))
MS = (raw_input('Masukkan Semester   : '))
MK = (raw_input('Masukkan Matakuliah : '))
JRS = (raw_input('Masukkan Jurusan   : '))
print
print"--------NILAI MAHASISWA--------"
A = (raw_input('Nilai Absent : '))
B = (raw_input('Nilai Tugas  : '))
C = (raw_input('Nilai Mid    : '))
D = (raw_input('Nilai Final  : '))
NA = float(A)
NT = float(B)
NMd = float(C)
NF = float(D)
TN = (NA + NT + NMd + NF) / 4
if (TN > 80):
    N = 'A'
    ket = 'Sangat Memuaskan'
elif(TN > 70):
    N = 'B'
    ket = 'Memuaskan'
elif(TN > 60):
    N = 'C'
    ket = 'Cukup'
elif(TN >= 40):
    N = 'D'
    ket = 'Kurang'
elif(TN < 40):
    N = 'E'
    ket = 'Tidak Lulus'
print
print"------BIODATA DAN NILAI ANDA------"
print"----------------------------------"
print"No. Induk Mahasiswa : ",(str(NS))
print"Nama Mahasiswa      : ",NM
print"Semester            : ",MS
print"Mata Kuliah         : ",MK
print"Jurusan             : ",JRS
print
print"Nilai Akhir         : " + format(TN,'.2f')
print"Nilai               : ",N
print"Keterangan          : ",ket
'''
