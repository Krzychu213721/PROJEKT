# PLANSZA
pole = [['-', '-', '-'],
           ['-', '-', '-'],
           ['-', '-', '-']]

def wyswietl_plansze():
    for wiersz in pole:
        print(' '.join(wiersz))

#WOLNE CZY ZAJĘTE
def czy_wolne(x, y):
    if pole[x][y] == '-':
        return True
    else:
        return False

def koniec_gry():
    for i in range(3):
        if pole[i][0] == pole[i][1] == pole[i][2] != '-':
            return True
        if pole[0][i] == pole[1][i] == pole[2][i] != '-':
            return True
    if pole[0][0] == pole[1][1] == pole[2][2] != '-':
        return True
    if pole[0][2] == pole[1][1] == pole[2][0] != '-':
        return True

    for i in range(3):
        for j in range(3):
            if pole[i][j] == '-':
                return False


    return True
def gra():
    print("Witaj w grze 'Kółko i krzyżyk'!")
    gracz = 'X'
    while not koniec_gry():
        wyswietl_plansze()
        print(f"Gracz {gracz}, podaj swoje współrzędne (np. 1 2): ")
        x, y = map(int, input().split())

        if czy_wolne(x, y):
            pole[x][y] = gracz
            if gracz == 'X':
                gracz = 'O'
            else:
                gracz = 'X'
        else:
            print("To pole jest już zajęte. Podaj inne współrzędne.")

    wyswietl_plansze()

    if koniec_gry():
        print("Koniec gry!")
        if gracz == 'X':
            print("Gracz kółko wygrał!")
        else:
            print("Gracz krzyżyk wygrał!")
    else:
        print("Remis!")

gra()
#współrzędne (0,0) to kordy lewego górnego rogu i na pierwsza to Y a druga to X
