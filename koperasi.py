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
		barang = "buku tulis"
		nilai = "Rp. 5,000"
		harga = 5000
	elif kode == "2" :
		barang = "buku kotak"
		nilai = "Rp. 5,000"
		harga = 5000
	elif kode == "3" :
		barang = "buku gambar A3"
		nilai = "Rp. 13,000"
		harga = 13000
	elif kode == "4" :
		barang = "pulpen"
		nilai = "Rp. 3,000"
		harga = 3000
	elif kode == "5" :
		barang = "spidol"
		nilai = "Rp. 7,000"
		harga = 7000	
	elif kode == "6" :
		barang = "pensil"
		nilai = "Rp. 2,500"
		harga = 2500
	elif kode == "7" :
		barang = "penghapus"
		nilai = "Rp. 2,000"
		harga = 2000
	elif kode == "8" :
		barang = "penggaris"
		nilai = "Rp. 4,500"
		harga = 4500
	elif kode == "9" :
		barang = "sharpener"
		nilai = "Rp. 3,500"
		harga = 3500
	elif kode == "10" :
		barang = "tip-x"
		nilai = "Rp. 4,000"
		harga = 4000
	else : print("\nBarang tidak ditemukan di toko kami.")
	
	if kode=='1' or kode=='2' or kode=='3' or kode=='4' or kode=='5' or kode=='6' or kode=='7' or kode=='8' or kode=='9' or kode=='10':
		try :
			jumlah = int(input(f"\n\tanda ingin membeli {barang} sebanyak? : "))
			if jumlah > 0 :	
				for i in range(jumlah) :
					list_barang.append(barang)
					list_harga.append(nilai)
					harga_sementara = harga*jumlah
			else :
				break
			total += harga_sementara
			print("\nAda yang ingin dibeli lagi?")
			lagi = input("\n\tketik 1 untuk memilih lagi : ")
			if lagi != '1': break
		except ValueError :
			print("\nYang anda masukan bukan angka.")
			lagi = input("\tketik 1 untuk membeli ulang : ")
			if lagi != '1': break

	else :
		lagi = input("\n\tketik 1 untuk memilih ulang : ")
		if lagi != '1': break

if list_barang == [] :
	print("\nAnda tidak memilih barang apapun.")
else :
	if len(list_barang) > 4 :
		diskon = total * 0.05
		total -= diskon
		print("\nDiskon 5%! karena melakukan 5 atau lebih pembelian barang.\nPotongan harga senilai Rp.", diskon)
	print("\nBarang yang anda beli : ↓")
	print(list_barang, "\n")
	print("Harga semua barang yang dibeli :↓")
	print(list_harga, "\n")
	print(f"total harga yang harus dibayar : Rp. {total}")
	
	uang = int(input("\n\tmasukan pembayaran anda : Rp. "))
	if uang > total :
		print("\nAnda memiliki kembalian Rp.", uang - total)
	elif uang == total :
		print("\nAnda memberikan uang pas.")
	else :
		print("\nUang anda kurang Rp.", total - uang)
		print("Sebagai gantinya push up 20×, Itu akan melunasi hutang anda.")
	
print("\nTerimakasih telah berkunjung,\nCeritakan pengalaman anda tentang toko Dimaz.")


