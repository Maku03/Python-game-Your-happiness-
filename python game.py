#Zgadnij liczbę z przedziału 1 - 100 i zobacz czy masz szczęśćie
#Gra uwzględnia:liczbę prób, zakres szczęśćia, liczbę podanych błędnych liczb

#wykorzysztana biblioteka
from random import randint

#zmienne
los = (randint(1,100))
odp = -1
i = 0
x = 0

#Program
print("Zgadnil liczbę z przedziału 1 - 100")
while odp != los:
    i += 1
    odp = int(input("Podaj liczbę: "))
    if odp > 100 or odp < 1:
        print("Podałeś liczbę z poza zakresu(1-100")
        i -= 1
        x += 1
    elif odp > los :
        print("Wylosowana liczna jest mniejsza od twojej")
    elif odp < los:
        print("Wylosowana liczba jest większa od twojej")
print("Brawo! Odgadłeś za", i, "razem.")
if i == 1:
    print('Masz mega szczęśćie może zagraj w lotto =)')
elif i == 2:
    print('To bardzo dobry wynik :)')
elif i == 3 or i == 4:
    print('Twoje szczęście jest na niskim poziomie :(')
elif i == 5:
    print('Szczęście cie opusiło :(')
if x > 0:
    print('Nie zaliczne próby: ',x)