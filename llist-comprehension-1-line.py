#list comprehension - jesto sposob skladni pisania kodu dla list, set, tez dict
#to kod w 1 linijce, alternatywa dla petli for

#zadanie Cyfyry
# ze zbioru liczb digits, podniesc kazda liczbe do potegi drugiej
# i zapisz te nowe liczby do nowej zmiennej

# I sposob
digits = [1,3, 7,9]
new = []

for digit in digits:
    new.append(digit **2)

print(new)

# II sposob
new = [digit ** 2 for digit in digits]
print(new)


#zadanie 
# #Imiona damskie sprawdz lub meskie, podaj plec przy imieniu. wyjatek to Nel, Kuba i Beatrycze

name = 'Karolina'
## 1 sposob
gender = 'female' if name[-1] == 'a' else 'male'

print(name, gender)

## 2 sposob

for letter in name:
    if name[-1] == 'a':
        print('płeć: kobieta')
        break
    else:
        print('płeć: facet')
        break
print('KONIEC PROGRAMU')
 
##odpalaie kodu z terminala VSC to: shit + ctrl + p i wpisac Python: Select Interpreter, a pozniej na polu uruchomic prawym myszy lub zaznaczony tekst shift + enter

##odpalanie kodu w Pycharm to run lub shift + f10
