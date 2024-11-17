#list comprehension - jesto sposob skladni pisania kodu dla list
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