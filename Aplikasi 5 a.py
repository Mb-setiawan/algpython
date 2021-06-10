#nilai awal
re = "y"
#perulangan program
while re=="y" or re=="Y" or re2=="true":
    print ("===============================")
    print ("  Aplikasi [5a] Cek kelulusan")
    print ("===============================")
    
    #penginputan
    n = input(">> Masukkan nilai : ")
    
    #pengecekan
    if int(n)>=0 and int(n)<101:
        if int(n)>60: 
            sts = "Lulus"
        else: 
            sts = "Tidak Lulus"
            #output status
        print(sts)
    else:
        print ("Masukkan Nilai Angka 0 - 100")

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
    

