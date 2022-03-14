print("SELAMAT DATANG DI TOKO DIMAZ\n")
print("\n1. buku tulis\t  :	Rp. 5,000")
print("2. buku kotak\t  :	Rp. 5,000")
print("3. buku gambar A3 :	Rp. 13,000")
print("4. pulpen\t  :	Rp. 3,000")
print("5. spidol\t  :	Rp. 7,000")
print("6. pensil\t  :	Rp. 2,500")
print("7. penghapus\t  :	Rp. 2,000")
print("8. penggaris\t  :	Rp. 4,500")
print("9. sharpener\t  :	Rp. 3,500")
print("10. tip-x\t  :	Rp. 4,000")

list_barang = []
list_harga = []
total = 0

while True :	
	harga_sementara = 0
	kode = input("\nPilih nomor dari barang yang ingin anda beli : ")
	if kode == "1" :
		kode = "buku tulis"
		nilai = "Rp. 5,000"
		harga = 5000
	elif kode == "2" :
		kode = "buku kotak"
		nilai = "Rp. 5,000"
		harga = 5000
	elif kode == "3" :
		kode = "buku gambar A3"
		nilai = "Rp. 13,000"
		harga = 13000
	elif kode == "4" :
		kode = "pulpen"
		nilai = "Rp. 3,000"
		harga = 3000
	elif kode == "5" :
		kode = "spidol"
		nilai = "Rp. 7,000"
		harga = 7000	
	elif kode == "6" :
		kode = "pensil"
		nilai = "Rp. 2,500"
		harga = 2500
	elif kode == "7" :
		kode = "penghapus"
		nilai = "Rp. 2,000"
		harga = 2000
	elif kode == "8" :
		kode = "penggaris"
		nilai = "Rp. 4,500"
		harga = 4500
	elif kode == "9" :
		kode = "sharpener"
		nilai = "Rp. 3,500"
		harga = 3500
	elif kode == "10" :
		kode = "tip-x"
		nilai = "Rp. 4,000"
		harga = 4000
	else : print("\tBarang tidak ditemukan di toko kami.")
	
	jumlah = int(input(f"Anda ingin membeli {kode} sebanyak? : "))
	if jumlah > 0 :	
		for i in range(jumlah) :
			list_barang.append(kode)
			list_harga.append(nilai)
			harga_sementara = harga*jumlah
	else :
		break
	total += harga_sementara
	print("ada yang ingin dibeli lagi?")
	lagi = input("Ketik 'y' / 'yes' untuk memilih lagi : ")
	if lagi == "y" or lagi == "yes" :
		continue
	else :
		break

if list_barang == [] :
	print("\n\tAnda tidak memilih barang apapun.")
else :
	if len(list_barang) > 4 :
		diskon = total * 0.05
		total -= diskon
		print("\ndiskon 5%! karena melakukan 5 atau lebih pembelian barang.\nPotongan harga senilai Rp.", diskon)
	print("\nBarang yang anda beli : ↓")
	print(list_barang, "\n")
	print("Harga semua barang yang dibeli :↓")
	print(list_harga, "\n")
	print(f"total harga yang harus dibayar : Rp. {total}")
	
	uang = int(input("Masukan pembayaran anda : Rp. "))
	if uang > total :
		print("\n\tAnda memiliki kembalian Rp.", uang - total)
	elif uang == total :
		print("\n\tAnda memberikan uang pas.")
	else :
		print("\n\tUang anda kurang Rp.", total - uang, " !!")
		print("Sebagai gantinya push up 20×, Itu akan melunasi hutang anda.")
	
print("\nTerimakasih telah berkunjung,\nCeritakan pengalaman anda tentang toko Dimaz.")


