from luas.menu import main_menu
from luas.lingkaran import l_lingkaran
from luas.segitiga import l_segitiga
from luas.p_panjang import l_ppanjang

#Mencetak Menu
main_menu()

while True:
    pilih = int(input("Silahkan Pilih: "))
    if pilih == 1:
        l_lingkaran()
    elif pilih == 2:
        l_segitiga()
    elif pilih == 3:
        l_ppanjang()
    else:
        exit()