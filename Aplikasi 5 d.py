#nilai awal
re = "y"
#perulangan program
while re=="y" or re=="Y" or re2=="true":
    print ("=======================================")
    print ("  Aplikasi [5d] Penilaian Mahasiswa")
    print ("=======================================")
    #Penginputan
    n = input(">> Masukkan Anka Umur : ")
    #pegecekan
    if int(n)>=91 and int(n)<100:
        sts = "A"
    elif int(n)>=81 and int(n)<=91:
        sts = "B"
    elif int(n)>=71 and int(n)<=81:
        sts = "C"
    elif int(n)<71:
        sts = "D"
    else:
        sts = "Masukkan Nilai Angka 0-100"
    #output status
    print("Nilai Huruf Anda : ", sts)

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



