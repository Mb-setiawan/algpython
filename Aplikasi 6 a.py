#nilai awal
re = "y"
unit = 660000
qty=0
#perulangan program
while re=="y" or re=="Y" or re2=="true":
    print ("==============================================================")
    print ("  Aplikasi [6a] Menghitung Total Transaksi Pembelian Printer")
    print ("==============================================================")
    #Penginputan
    qty = input(">> Masukkan Jumlah Pembelian : ")
    #pegecekan
    if int(qty)>0:
        total=int(qty)*unit
        #output total
        print("Total Harga Transaksi : Rp.",total)
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



