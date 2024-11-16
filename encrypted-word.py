#szyfrowanie slow wg szyfru cezara 

     #ord przyjmuje liste, cyfre lub inny dowolny znak i zwraca przypisana liczbe wg tablicy ascii
     #chr zmienia spowrotem liczbe na znak, odwrotnosc ord
     # jesli przekroczy ostatni znak w alfabecie (jest icg 26) to wtedy ma cofnac sie na poczatek zeby nie bylo znakow spejclanych
     # key to informacja o ile liter przesuwamy sie w alfabecie
     #algorytm poprawnie tez szyfruje spacje i inne znaki spoza alfabetu, wiec 1 if przepisuje nierozpoznane znaki
     # ASCII (ang. American Standard Code for Information Interchange) to standard kodowania znaków
     
def encrypted(message, key):
    encrypted = ''
    
    for letter in message:
        #dla malych liter
        if ord(letter) < ord('a') or ord(letter) > ord('z'):
            encrypted += letter
        elif ord(letter) + key > ord('z'):
            encrypted += chr(ord(letter) + key - 26)
        else:
            encrypted += chr(ord(letter) + key)
    return encrypted
     
     
print(encrypted('ZakoDowane', 3))


#algorytm odszyfrowania

#musimy odszyfrowac wiec zamiast dodawac key zeby do przodu isc to musimy odejmowac aby sie cofnac do zrodla

def deencrypt(message, key):
    encrypted = ''
    
    for letter in message:
        if ord(letter) < ord('a') or ord(letter) > ord('z'):
            encrypted += letter
        elif ord(letter) - key < ord('a'):
            encrypted += chr(ord(letter) - key + 26)
        else:
            encrypted += chr(ord(letter) - key)
    return encrypted
     
     
print(deencrypt('ZdnrDrzdqh', 3))



###

print(ord('a'))  # Wynik: 97 (kod ASCII dla 'a')
print(ord('A'))  # Wynik: 65 (kod ASCII dla 'A')
print(ord('Z'))  # Wynik: 90 (kod ASCII dla 'Z')
print(ord('ą'))  # Wynik: 261 (kod Unicode dla 'ą')

print(chr(97))  # Wynik: 'a' (znak dla kodu ASCII 97)
print(chr(65))  # Wynik: 'A' (znak dla kodu ASCII 65)
print(chr(90))  # Wynik: 'Z' (znak dla kodu ASCII 90)
print(chr(261))  # Wynik: 'ą' (znak dla kodu Unicode 261)
