# jak sciagam na swoj komputer pythona i go instaluje to znaczy,ze intaluje wtedy tez z nim pvm i kompilator?
#
# Tak, dokładnie! Kiedy pobierasz i instalujesz Pythona na swoim komputerze, instalujesz kompletny zestaw narzędzi, w tym zarówno kompilator, jak i Python Virtual Machine (PVM). Te komponenty razem umożliwiają działanie Pythona i uruchamianie programów napisanych w tym języku. Oto jak to działa:
#
# Co instaluje Python?
# Interpreter (Python):
#
# To główny program, który odpowiada za uruchamianie skryptów Pythona.
# Jest to program, który rozumie i wykonuje kod źródłowy w Pythonie. Po zainstalowaniu Pythona, masz dostęp do interpretera (komendy python lub python3 w terminalu), który pozwala uruchamiać programy napisane w tym języku.
# Kompilator:
#
# Kompilator Pythona przekształca kod źródłowy (plik .py) do bytecode'u (plik .pyc), który jest następnie wykonywany przez PVM. Kompilacja do bytecode'u odbywa się automatycznie podczas uruchamiania programu, jeśli to konieczne. Na przykład, jeśli uruchomisz plik .py, Python skompiluje go do .pyc i zapisze w katalogu __pycache__.
# Kompilacja ma na celu przyspieszenie działania programu, ponieważ bytecode jest szybszy do wykonania niż kod źródłowy.
# Python Virtual Machine (PVM):
#
# To komponent, który odpowiada za wykonywanie bytecode'u. PVM interpretuje bytecode wygenerowany przez kompilator Pythona i uruchamia go na twoim systemie. PVM jest częścią interpretera i jest odpowiedzialna za to, co się dzieje, gdy uruchamiasz kod.
# Standardowa biblioteka Pythona:
#
# Python zawiera również bibliotekę standardową, która oferuje gotowe funkcje i moduły do różnych zadań (np. manipulacja plikami, operacje na tekstach, sieci, obsługa danych itp.).
# Jak to działa w praktyce?
# Pisanie kodu:
#
# Piszesz skrypt Pythona w pliku .py. Na przykład:
# python
# Copy code
# # program.py
# print("Hello, World!")
# Uruchamianie programu:
#
# Kiedy uruchomisz skrypt (np. python program.py), Python:
# Sprawdza, czy istnieje skompilowany plik bytecode (plik .pyc). Jeśli go nie ma, kompiluje kod źródłowy do bytecode'u.
# Kompiluje kod do bytecode (jeśli to konieczne).
# Bytecode jest następnie wykonywany przez PVM.
# PVM wykonuje bytecode:
#
# PVM interpretuje bytecode i wykonuje instrukcje. W przypadku programu program.py, PVM wykona polecenie print("Hello, World!"), wyświetlając wynik na ekranie.
# Podsumowanie:
# Kiedy instalujesz Pythona, instalujesz kompletny interpreter zawierający zarówno kompilator, jak i PVM.
# Kompilator przekształca kod źródłowy do bytecode'u.
# PVM wykonuje bytecode na twoim komputerze.
# Te komponenty razem umożliwiają uruchamianie programów w Pythonie.