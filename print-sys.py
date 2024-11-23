#print

#argument sep umozliwia okreslenie co byc miedzy obiektami
print(1, 2, 5, 7, sep='-/-')

#argument end domyslnie jest ze ustawiony od nowej lini dlatego print zawsze jest od nowej lini end='\n'
print(1, 2, 5, 7, end='\n')
print(1, 2, 5, 7, end='')
print(1, 2, 5, 7, end='')

#miejsce do ktorego wypisze sie tekst, domyslnie to sys.stdout - czyli konsola
print(1, 2, 5, 7, file='sys.stdout')


#flush okresla czy tekst ma byc splukany, domyslnie na Fals
print(1, 2, 5, 7, flush=True)

# import sys
# print("Wersja Pythona:", sys.version)
# print("System operacyjny:", sys.platform)
# print("Interpreter znajduje się pod:", sys.executable)

#Moduł sys to interfejs do wnętrza Pythona i jego środowiska uruchomieniowego. Przydaje się w sytuacjach, gdy potrzebujesz precyzyjnej kontroli nad programem lub jego interakcjami z użytkownikiem i systemem operacyjnym.
#sys to wbudowany moduł w Pythonie, który dostarcza funkcje i zmienne do interakcji z interpreterem Pythona.

#Interpreter Pythona to program, który wykonuje kod napisany w języku Python, linia po linii, tłumacząc go na instrukcje zrozumiałe dla komputera. W przeciwieństwie do języków kompilowanych (jak C czy Java), Python jest językiem interpretowanym, co oznacza, że kod nie jest kompilowany w całości przed wykonaniem, lecz interpretowany w czasie rzeczywistym.


###co sie dzieje z kodem

# Oto diagram ilustrujący proces działania Python Virtual Machine (PVM) na przykładzie:

# Kod źródłowy jest pisany przez programistę w Pythonie.
# Interpreter Pythona odbiera kod źródłowy i analizuje go.
# Kod jest kompilowany do formatu bajtowego (bytecode), co jest etapem pośrednim.
# Kod bajtowy może być zapisany w pliku .pyc w folderze __pycache__.
# PVM wczytuje kod bajtowy do pamięci.
# PVM interpretuje instrukcje bajtowe krok po kroku.
# Instrukcje są wykonywane, a wyniki (np. dane wyjściowe) są wyświetlane.


#sposoby drukowania print z zajec - zjazd 2
a = 3
b = 'ala'
pi =3.24
# print(a * b)

print(str(a) +b)
print(a,b, sep='', end='\n') #n przejsice do nowej lini
print(a,b, sep='-', end='\t') #przerwa miedzy elementami, tabulator
print(a,b, sep='-', end='+')
print(a,b, sep='-', end='+\n')
print(f'testest {b} {pi}')  #nie drukuje zmiennej tylko zawartosc zmiennej


print(f'{pi:.100f}')  #okreslac ile miejsc po przecinku, 
#okresla format wydruku liczby, czyli 100 miejsc poprzecinku tutaj, #f stringi w pythonie


