'''
batas atas
'''
'''
#contoh pengulangan for sederhana
angka = [1,2,3,4,5]
for x in angka:
    print x
'''
'''
#contoh perulangan for
buah = ["nanas", "apel", "jeruk"]
for makanan in buah:
    print("saya suka makan", makanan)
'''
'''
#contoh penggunaan while loop
count = 0
while(count < 11):
    print('the count is : ',count)
    count = count + 1

print("good bye!")
'''
'''
#contoh penggunaan nested loop
i = 2
while(i < 100):
    j = 2
    while(j <= (i/j)):
        if not (i%j): break
        j = j +1
    if (j > i/j) : print(i, "is prime")
    i = i + 1

print "good bye!"
'''
'''
name = 'john doe'
message = "john doe belajar bahasa python di belajarpython.com"
print("name[0] : ",name[0])
print("message[2:8] : ",message[2:8])
'''
'''
panjang = 100
lebar = 21.5
nama = "umar"
print panjang
print lebar
print nama
'''
'''
#cara mengakses nilai di dalam list python
list1 = ['fisika', 'kimia', 1993, 2017]
list2 = [1,2,3,4,5,6,7]

print("list1[0] : ",list1[0])
print("list2[1:5] : ",list2[1:5])
'''
'''
list = ['fisika', 'kimia', 1993, 2017]
print("nilai ada pada index 2 : ",list[2])

list[2] = 2001
print("nilai baru ada pada index 2 : ",list[2])
'''
'''
#contoh cara menghapus list pada python
list1 = ['fisika', 'kimia', 1993, 2017]

print (list1)
del list1[2]
print ("setelah dihapus pada index 2 : ", list1)
'''
'''
list1 = ['fisika', 'kimia', 1993, 2017]
list2 = [1,2,3,4,5,6,7]
print len(list1)
print list1 + list2
print list1 * 2
print 2 in [1,2,3]
'''
'''
tup1 = (12,34,56)
tup2 = ('abc','xyz')
tup3 = tup1 + tup2
print tup3
'''
'''
tup = ('fisika','kimia',1993,2017)

print (tup)
del tup
print "setelah menghapus tuple : "
print tup
'''
'''
#contoh cara membuat dictionary pada python
dict = {'nama': 'near', 'age': 7, 'class': 'first'}
print("dict['nama']: ",dict['nama'])
print("dict['age']: ",dict['age'])
'''
'''
dict1 = {'nama': 'near', 'age': 7, 'class': 'first'}
dict1['age'] = 8;
dict1['school'] = "dps school"
print("dict['age']: ", dict1['age'])
print("dict1['school']: ", dict1['school'])
print dict1
'''
'''
#contoh cara menghapus pada dictionary python
dict1 = {'nama': 'near', 'age': 7, 'class': 'first'}
#del dict1['nama']
#print dict1
#dict1.clear()
#print dict1
#del dict1
print("dict1['age']: ", dict1['age'])
print("dict1['school']: ", dict1['school'])
'''
'''
dict1 = {'nama': 'near', 'age': 7, 'class': 'first'}
print len(dict1)
print str(dict1)
'''
'''
import time;
#ticks = time.time()
#print "jam", ticks
#localtime = time.localtime(time.time())
#print "waktu local saat ini : ", localtime
localtime1 = time.asctime(time.localtime(time.time()))
print "waktu local saat ini : ", localtime1
'''
'''
import calendar
cal = calendar.month(2018, 3)
print "dibawah ini adalah calender : "
print cal
'''
'''
def printme(str1):
    "this prints a passed string into this function"
    print(str1)
    return
'''
'''
def print_func(par):
    print "hallo : ",par
    return
'''
'''
x = 5
print(x, "tipenya adalah", type(x))
x = 2.0
print(x, "tipenya adalah", type(x))
x = 1+2j
print (x, "tipenya adalah", type(x))
'''
'''
d = {1:'satu', 2:'dua', 'tiga':3}
print(type(d))
print("d[1] = ", d[1])
print("d[tiga] = ", d['tiga'])
print("d[3] = ", d[3])
'''
'''
#list number
number = [7,5,9,8,4,2,6,4,1]
#variabel untuk menyimpan jumlah
sum = 0
#literasi
for each in number:
    sum = sum + each
#output : jumlah keseluruhannya : 46
print ("jumlah keseluruhannya: ",sum)
'''
'''
count = 1
while (count <= 5):
    print("algoritma dan pemrograman")
    count = count + 1
'''
'''
i = 1
while (i <= 11):
    print (i)
    i = i + 2
'''
'''
for i in range(1,10):
    print (i)
'''
'''
var1 = "hello python!"
var2 = var1[:6]
print("string update: - ", var1[:6] + 'world')
'''
'''
str1 = "hello"
str2 = "python"
#menggunakan +
print('str1 +str2 =', str1 + str2)
#menggunakan *
print('str1 * 3 =', str1 * 3)
'''
'''
#menggunkan posisi default
#default_order = "{}, {},{}".format("budi","galih","ratna")
#print('\n----Urutan Default----')
#print(default_order)
#menggunakan argument posisi
#positional_order = "{1}, {0}, dan {2}".format("budi", "near", "indra")
#print(positional_order)
#menggunkan argument kata kunci
keyword_order = "{r}, {b} dan {g}".format("budi", "near", "indra")
#print('\n----Urutan Berdasarkan kata kunci----')
print(keyword_order)
'''
'''
ganjil = [1,3,4,7,9]
#ganjil[2] = 5
#print(ganjil)
ganjil[2:5] = [11,13,15]
print ganjil
'''
'''
import math
a = int(raw_input("masukkan a : "))
b = int(raw_input("masukkan b : "))
c = int(raw_input("masukkan c : "))
d = (b**2) - (4*a*c)
x1 = (-b+math.sqrt(d))/(2*a)
x2 = (-b-math.sqrt(d))/(2*a)
print('solusinya adalah {0} dan {1}'.format(x1, x2))
'''
'''
my_list = ['p','y','t','h','o','n','i','n','d','o']
del my_list[2]
print my_list
'''
'''
alfabet = ['a','b','d','f','e','c','h','g','j','i']
#alfabet.sort()
#print(alfabet)
alfabet.sort(reverse=True)
print(alfabet)
'''
'''
nama = ('galih', 'ratna')
for nama in nama:
    print('hi', nama)
'''
'''
def sapa(nama):
    print("hai," + nama + ".Apa Kabar?")
#sapa("umar")
sapa("near")
'''
huruf = raw_input("masukkan sebuah huruf : ")
if (huruf >= 'A'):
    if (huruf <= 'Z'):
        print "ini adalah huruf besar"
    elif (huruf >= 'a'):
        if (huruf <= 'z'):
            print "ini adalah huruf kecil"
        else:
            print "huruf > z"
    else:
        print "huruf > z tapi < a"
else:
    print "huruf < A"
