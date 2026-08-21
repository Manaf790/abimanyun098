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



nilai = 88

match True:
    case _ if nilai >= 90:
        print("Nilai Anda A.")
    case _ if nilai >= 80:
        print("Nilai Anda B.")
    case _ if nilai >= 70:
        print("Nilai Anda C.")
    case _:
        print("Nilai Anda D.")