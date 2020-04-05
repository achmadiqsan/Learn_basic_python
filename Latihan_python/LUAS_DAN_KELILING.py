from math import pi, sqrt

def lingkaran():
    r = raw_input('Lingkaran,\nMasukkan Jari-Jari : ')
    r = float(r)
    luas = pi*r**2
    keliling = 2*pi*r
    print
    print('Luas Lingkaran = '+format(luas,'.2f'))
    print('keliling Lingkaran = '+format(keliling,'.2f'))

#lingkaran()

def bujursangkar():
    r = raw_input('Bujursangkar,\nMasukkan Panjang Sisi : ')
    r = float(r)
    luas = r**2
    keliling = 4*r
    print
    print('Luas Bujursangkar = '+format(luas,'.2f'))
    print('Keliling Bujursangkar = '+format(keliling,'.2f'))

#bujursangkar()

def persegipanjang():
    p = raw_input('Persegi Panjang,\nMasukkan Panjang : ')
    l = raw_input('Masukkan Lebar : ')
    p = float(p)
    l = float(l)
    luas = p*l
    keliling = 2*(p+l)
    print
    print('Luas Persegi Panjang = '+format(luas,'.2f'))
    print('Keliling Persegi panjang = '+format(keliling,'.2f'))

#persegi()

def segitiga():
    a = raw_input('Segitiga Siku-Siku, \nMasukkan Alas : ')
    t = raw_input('Masukkan Tinggi : ')
    a = float(a)
    t = float(t)
    luas = 0.5*a*t
    keliling = a+t+sqrt(a**2+t**2)
    print
    print('Luas Segitiga = '+format(luas,'.2f'))
    print('Keliling Segitiga = '+format(keliling,'.2f'))

#segitiga()

def persegi():
    s = raw_input('Persegi,\nMasukkan Sisi : ')
    s = float(s)
    luas = s * s
    keliling = 4 * s
    print
    print('Luas Persegi = '+format(luas,'.2f'))
    print('Keliling Persegi = '+format(keliling,'.2f'))

#persegi()

def jajargenjang():
    a = raw_input('Jajaran Genjang,\nMasukkan Alas : ')
    sm = raw_input('Masukkan Sisi Miring : ')
    t = raw_input('Masukkan Tinggi : ')
    a = float(a)
    sm = float(sm)
    t = float(t)
    luas = a * t
    keliling = 2 * (a + sm)
    print
    print('Luas Jajaran Genjang = '+format(luas,'.2f'))
    print('Keliling Jajaran Genjang = '+format(keliling,'.2f'))

#jajargenjang()

def belahketupat():
    s = raw_input('Belah Ketupat,\nMasukkan Sisi : ')
    d1 = raw_input('Masukkan Diagonal 1 : ')
    d2 = raw_input('Masukkan Diagonal 2 : ')
    s = float(s)
    d1 = float(d1)
    d2 = float(d2)
    luas = 4 * s
    keliling = (d1 * d2)/2
    print
    print('Luas Belah Ketupat = '+format(luas,'.2f'))
    print('Keliling Belah Ketupat = '+format(keliling,'.2f'))

#belahketupat()

def trapesium():
    sa = raw_input('Trapesium,\nMasukkan Sisi Atas : ')
    sb = raw_input('Masukkan Sisi Bawah : ')
    sm = raw_input('Masukkan Sisi Miring : ')
    t = raw_input('Masukkan Tinggi : ')
    sa = float(sa)
    sb = float(sb)
    sm = float(sm)
    t = float (t)
    sasb1 = (sa + sb)* t
    luas =  sasb1 / 2
    keliling = sa + sb + sm + t
    print
    print('Luas Trapesium = '+format(luas,'.2f'))
    print('Keliling Trapesium = '+format(keliling,'.2f'))

#trapesium()

def layanglayang():
    s1 = raw_input('Layang-layang,\nMasukkan Sisi Pertama : ')
    s2 = raw_input('Masukkan Sisi Kedua : ')
    d1 = raw_input('Masukkan Diagonal 1 : ')
    d2 = raw_input('Masukkan Diagonal 2 : ')
    s1 = float(s1)
    s2 = float(s2)
    d1 = float(d1)
    d2 = float(d2)
    luas = (d1 * d2)/2
    keliling = 2 * (s1 + s2)
    print
    print('Luas Layang-layang = '+format(luas,'.2f'))
    print('Keliling Layang-layang = '+format(keliling,'.2f'))

#layanglayang()

print '''
===================================================
PROGRAM MENGHITUNG LUAS DAN KELILING BANGUN DATAR :
===================================================
1. LINGKARAN
2. BUJUR SANGKAR
3. PERSEGI PANJANG
4. SEGITIGA SIKU-SIKU
5. PERSEGI
6. JAJARAN GENJANG
7. BELAH KETUPAT
8. TRAPESIUM
9. LAYANG-LAYANG
10. EXIT
'''
#x = raw_input('Pilihan Anda : ')

#while x :
   # if x=='1':
        #lingkaran()
    #elif x=='2':
        #bujursangkar()
    #elif x=='3':
        #persegi()
    #elif x=='4':
        #segitiga()
    #else:
        #print
        #print('TERIMA KASIH SUDAH MENGGUNAKAN PROGRAM INI')
        #break
    #x = raw_input('\nCoba Yang Lain?\Pilihan Anda : ')

x = raw_input('Pilihan Anda : ')
print('=========================')

while x :
    if x=='1':
        lingkaran()
    elif x=='2':
        bujursangkar()
    elif x=='3':
        persegipanjang()
    elif x=='4':
        segitiga()
    elif x=='5':
        persegi()
    elif x=='6':
        jajargenjang()
    elif x=='7':
        belahketupat()
    elif x=='8':
        trapesium()
    elif x=='9':
        layanglayang()
    elif x=='10':
        print
        print('TERIMA KASIH SUDAH MENGGUNAKAN PROGRAM INI')
        break
    else:
        print('PILIHAN YANG ANDA MASUKKAN TIDAK TERDAFTAR DI MENU')
    x = raw_input('\nCoba Yang Lain?\nPilihan Anda : ')
    print('========================================================')

raw_input()
