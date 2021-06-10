#nilai awal
re = "y"
harga = 660000
qty=0
disc=0.15
bayar=0
totaldisc=0
#perulangan program
while re=="y" or re=="Y" or re2=="true":
    print("==============================================================")
    print("  Aplikasi [6a] Menghitung Total Transaksi Pembelian Printer")
    print("==============================================================")
    #Penginputan
    qty = input(">> Masukkan Jumlah Pembelian : ")
    #pegecekan
    if int(qty)>0:
        total=int(qty)*harga
        #output total
        if total>1500000:
            totaldisc=total*disc
            bayar=total-totaldisc
            print ("anda mendapat potongan harga 15%")
            print ("Harga Sebelumnya : ",total)
            print ("Potongan Harga   : ",totaldisc)
        else:
            bayar=total
        print("==============================================================")
        print("Harga Bayar : Rp.",bayar)
    else:
        print("Minimal Pembelian Adalah 1")
        
    #konfirmasi perulangan program
    re2="false"
    while re2=="false":
        re = input("Ulangi Program? y/t : ")
        if re=="t" or re=="T":
            break
        elif re=="y" or re=="Y":
            re="y"
            re2="true"
        else:
            re2="false"



