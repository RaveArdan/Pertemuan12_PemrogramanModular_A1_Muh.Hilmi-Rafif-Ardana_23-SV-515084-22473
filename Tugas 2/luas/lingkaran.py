from luas.menu import main_menu

def l_lingkaran():
    print("Menghitung Luas Lingkaran")
    r = int(input("Masukkan Jari-Jari : "))
    luas = 3.14*(r**2)
    print(f"Luas Lingkaran adalah {luas} cm")
    print()
    print("Coba lagi [Y/N]? ")
    back = input().upper()
    if back == ("Y"):
        main_menu()
    else:
        exit()

        