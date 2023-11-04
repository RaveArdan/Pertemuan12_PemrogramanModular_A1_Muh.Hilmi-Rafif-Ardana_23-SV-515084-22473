from luas.menu import main_menu

def l_ppanjang():
    print("Menghitung Luas Persegi Panjang")
    p = int(input("Masukkan Panjang : "))
    l = int(input("Masukkan Lebar : "))
    luas = p*l
    print(f"Luas Persegi Panjang adalah {luas} cm")
    print()
    print("Coba lagi [Y/N]? ")
    back = input().upper()
    if back == ("Y"):
        main_menu()
    else:
        exit()