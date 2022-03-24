#membuat garis
def garis ():
    print ("--------------------------------")

#fungsi buble ascending ( dari kecil ke besar )
def sort_asc(array):
    array = sorted(array)
    return(array)

#fungsi buble descending ( dari besar ke kecil )
def sort_desc(array):
    array = sorted(array, reverse = True)
    return(array)

#fungsi rata-rata
def rata_rata(angka):
    return sum(angka)/len(angka)

#input nilai
garis()
print("Masukan tiga buah nilai")
#masukan tipe data integer
nilai_a = int(input("Nilai A : "))
nilai_b = int(input("Nilai B : "))
nilai_c = int(input("Nilai C : "))
#masukan ke tipe data array
angka = [nilai_a, nilai_b, nilai_c]

#nilai akhir
print("Hasil Akhir")
print("Urutan Angka ascending : ",(sort_asc(angka)))
print("Urutan Angka descending : ",(sort_desc(angka)))

#cari nilai terbesar (max)
print ("Angka Terbesar : ",max(angka))

#cari nilai terkecil (min)
print ("Angka Terkecil : ",min(angka))

#cari nilai rata-rata
print ("Rata-ratanya : ",round(rata_rata(angka),2))
