#szyfrowanie slow wg szyfru cezara 

#ord przyjmuje liste, cyfre lub inny dowolny znak i zwraca przypisana liczbe wg tablicy ascii
     #chr zmienia spowrotem liczbe na znak
     # jesli przekroczy ostatni znak w alfabecie (jest icg 26) to wtedy ma cofnac sie na poczatek zeby nie bylo znakow spejclanych
     # key to informacja o ile liter przesuwamy sie w alfabecie
     #algorytm poprawnie tez szyfruje spacje i inne znaki spoza alfabetu, wiec 1 if przepisuje nierozpoznane znaki
     
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
