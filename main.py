import getpass

def menu():
    print("\n\t======================================")
    print("\n\t-------Pilihan----------")
    print("\t1. Calculator")
    print("\t2. Pembayaran")
    print("\t3. Penilaian")

    pilih = input ("\n\tMasukan pilihan :")
    if pilih == "1" :
        from Perhitungan.calculator import calculator
        tanya()
        
    elif pilih == "2" :
        from Perhitungan.pembayaran import pembayaran
        tanya()
    elif pilih == "3" :
        from Perhitungan.penilaian import penilaian
        tanya()
    else:
        tanya()

def tanya():
    tanya = input("\n\tKembali ke menu pilihan (y/t)?")
    if tanya == "y" :
        menu()

    elif tanya == "t" :
        exit
    else:
        print ("\n\tSalah input..........!!!")

username = input("\nusername : ")
password = getpass.getpass()
print("===============================================")

if username == "nida" and password == "1796" :
    menu()

else:
    print ("maaf password atau username ini salah............!!!")
           
menu()



