#nilai awal
re = "y"
#perulangan program
while re=="y" or re=="Y" or re2=="true":
    print ("===================================")
    print ("  Aplikasi [5b] Cek Tingkat Usia")
    print ("===================================")
    #Penginputan
    u = input(">> Masukkan Anka Umur : ")
    #pegecekan
    if int(u)>0 and int(u)<101:
        if int(u)>=60:
            sts = "Lansia"
        elif int(u)>=35 and int(u)<=59:
            sts = "Dewasa"
        elif int(u)>=18 and int(u)<=34:
            sts = "Pemuda"
        elif int(u)>=15 and int(u)<=17:
            sts = "Remaja"
        else:
            sts = "Anak-anak"
            #output status
        print("Status Usia Anda : ", sts)
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



