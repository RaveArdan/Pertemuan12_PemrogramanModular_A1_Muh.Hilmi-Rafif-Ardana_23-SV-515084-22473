from luas.menu import main_menu

def l_segitiga():
    print("Menghitung Luas Segitiga")
    a = int(input("Masukkan Alas : "))
    t = int(input("Masukkan Tinggi : "))
    luas = (a*t)/2
    print(f"Luas Segitiga adalah {luas} cm")
    print()
    print("Coba lagi [Y/N]? ")
    back = input().upper()
    if back == ("Y"):
        main_menu()
    else:
        exit()