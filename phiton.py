#jumlah_buku = 3
#harga_buku = 45000
#jumlah_pulpen = 2
#harga_pulpen = 7500
#jumlah_tas = 1 
#harga_tas = 120000
#Diskon = 0.1
#total_belanja = (jumlah_buku * harga_buku) + (jumlah_pulpen * harga_pulpen) + (jumlah_tas * harga_tas)
#print("Total belanja: Rp", total_belanja)      
#total_belanja -= total_belanja * Diskon
#print("Total belanja setelah diskon: Rp", total_belanja)



#tabungan = 50000
#tabungan *= 3
#tabungan -= 30000
#tabungan += 50000
#print("Total tabungan: Rp", tabungan)



#umur = 18

#if umur >= 17:
#    print("Anda sudah cukup umur untuk membuat KTP.")



#umur = 18

#if umur >= 17:
    #print("Anda sudah cukup umur untuk membuat KTP.")
#else:
    #print("Anda belum cukup umur untuk membuat KTP.")



#nilai = 85
#if nilai == 100:
#    print("Nilai Anda sempurna.")
#elif nilai >= 75:
#   print("Anda lulus.")
#else:
#    print("Anda tidak lulus.")



#niliai = 85
#if nilai >= 90:
#    print("Nilai Anda A.")
#elif nilai >= 80:   
#    print("Nilai Anda B.")  
#elif nilai >= 70:
#    print("Nilai Anda C.")
#else:
#    print("Nilai Anda D.")



#nilai = 88

#match True:
#    case _ if nilai >= 90:
#        print("Nilai Anda A.")
#    case _ if nilai >= 80:
#        print("Nilai Anda B.")
#    case _ if nilai >= 70:
#        print("Nilai Anda C.")
#   case _:
#        print("Nilai Anda D.")    



# rows = 5
# for i in range(1, rows + 1):
#  print(" " * (rows -i) + "*" * (2 * i - 1))



# rows = 5
# while rows >= 1:
#    print("*" * rows)
#    rows -= 1



rows = 5
i = 1
while i <= rows:
    print(" " * (rows - i) + "*" * i)
    i += 1



#def luaspersegi(sisi):
#    return sisi * sisi

#print(luaspersegi(4))


#def ganjilgenap(angka):
#    if angka % 2 == 0:
#        return "Genap"
#    else:
#        return "Ganjil"

#print(("Cek Ganjil Genap: "), ganjilgenap (6))
#print(("Cek Ganjil Genap: "), ganjilgenap (7))



#def konversi_suhu(celcius):
#    fahrenheit = (celcius * 1.8) + 32
#    return fahrenheit
#
#print(("Konversi Suhu: "), konversi_suhu(20),"Fahrenheit")



#nama = input("Masukkan nama: ")
#umur = int(input("Masukkan umur: "))

#print(f"Halo {nama}, umur kamu {umur} tahun.")



# def hitungTabungan(hari):
#    total = 0
#    for h in range(1, hari + 1):
#        if h%2!=0:
#            total += 2000
#        else:
#            total += 5000

#    return total

# print(hitungTabungan(3))



# def cekTilang(plat, tanggal):
#    if plat % 2 == 0 and tanggal % 2 == 0:
#        return "Anda Aman."
#    elif plat % 2 == 1 and tanggal % 2 == 1:
#            return "Anda Aman."
#    elif plat % 2 == 1 and tanggal % 2 == 0:
#        return "Anda Ditilang."
#    elif plat % 2 == 0 and tanggal % 2 == 1:
#            return "Anda Ditilang."

# print(cekTilang(24, 12))
# print(cekTilang(13, 20))



# def hitungKopi(jumlahGelas):
#    hargaGelas = 5000
#    totalHarga = jumlahGelas * hargaGelas

#    if jumlahGelas >= 3:
#        totalHarga -= totalHarga * 0.1 

#    return totalHarga


# print(hitungKopi(2))
# print(hitungKopi(4))



# def tepokNyamuk(jumlah):
#     for angka in range(1, jumlah + 1):
#         if angka % 3 == 0:
#             print("TEPOK")
#         else:
#             print(angka)

# print(tepokNyamuk(5))
    


