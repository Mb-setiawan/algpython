#nilai awal
re = "y"
#perulangan program
while re=="y" or re=="Y" or re2=="true":
    print ("=======================================")
    print ("  Aplikasi [5c] Cek Nilai huruf 0-100")
    print ("=======================================")
    #Penginputan
    n = input(">> Masukkan Anka Umur : ")
    #pegecekan
    if int(n)>0 and int(n)<101:
        if int(n)>80:
            sts = "BAIK SEKALI"
        elif int(n)>=65:
            sts = "BAIK"
        elif int(n)>=55:
            sts = "CUKUP"
        elif int(n)>=40:
            sts = "KURANG"
        else:
            sts = "KURANG SEKALI"
        #output status
        print("Nilai Huruf Anda : ", sts)
    else:
        print("Masukkan Umur Angka 1-100 saja")
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



