print("=============warung pa jum=============")
print("=======makanan enak,harga bersahabat=======")
print("============ TERIMA KASIH ============")


pembeli = input("Masukkan nama Pembeli: ")
print ("Nama Pembeli :", pembeli) 

total1=0
jenis1=""
porsi=0
gelas=0

def fungsimakanan():
   global total1
   global porsi
   global jenis1
   print ("\n~~Menu Makanan")
   print("1. ikan nila bakar - Rp15000")
   print("2. ikan gurame saos padang - Rp56000")
   print("3. ikan nila bumbu manis - Rp20000")
   nomor=int(input("Masukan Pilihan: "))
   porsi= int(input("Berapa Porsi: "))
   
   if nomor==1:
       total1=porsi*15000
       print (porsi,"porsi Ayam Geprek = Rp", total1)
       jenis1=("Ayam Geprek")
   elif nomor==2:
       total1=porsi*18000
       print (porsi,"porsi ikan gurame saos padang  = Rp", total1)
       jenis1=("ikan gurame saos padang")
   elif nomor==3:
       total1=porsi*20000
       print (porsi, "ikan nila bumbu manis = Rp", total1)
       jenis1=("ikan nila bumbu manis")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsimakanan()


fungsimakanan()

total2=0
jenis2=""

def fungsiminuman():
   global total2
   global jenis2
   global gelas
   print("\n~~Menu Minuman")
   print("1. lemon tea - Rp8000")
   print("2. milkshake - Rp8500")
   print("3. mineral - Rp5000")
   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas: "))

   if nomor==1:
       total2=gelas*6000
       print (gelas," lemon tea = Rp", total2)
       jenis2=("lemon tea")
   elif nomor==2:
       total2=gelas*8500
       print (gelas, " milkshake = Rp", total2)
       jenis2=("milkshake")
   elif nomor==3:
       total2=gelas*10000
       print (gelas, " mineral = Rp", total2)
       jenis2=("mineral")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsiminuman()


fungsiminuman()
    
totalsemua=0
totalsemua=total1+total2
print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp."))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n=====================================")
print("======= S T R U K   B E L I =========")
print("=====================================")
print (" Nama               :",pembeli)
print (" Beli               :",porsi,jenis1,"-", total1)
print ("                    ",gelas,jenis2,"-", total2)
print (" Tagihan            : Rp.",totalsemua)
print (" Uang               : Rp.",uang)
print (" Kembalian          : Rp.",kembalian)
print("===========================")
print("===========================")