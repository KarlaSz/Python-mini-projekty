# Co to jest kompilacja w Pythonie?
# Kompilacja w kontekście Pythona oznacza proces przekształcania kodu źródłowego napisanego w Pythonie (plik .py) na bytecode — pośrednią formę, którą interpreter Python (znany jako Python Virtual Machine, PVM) jest w stanie wykonać. Jest to ważne, ponieważ Python jest językiem interpretowanym, a nie skompilowanym, co oznacza, że kod źródłowy jest tłumaczony i wykonywany na bieżąco przez interpreter.

# Kompilacja w Pythonie to proces, w którym kod źródłowy (.py) jest tłumaczony do bytecode'u (plik .pyc).
# Bytecode to pośrednia reprezentacja kodu, która jest wykonywana przez Python Virtual Machine (PVM).
# Kompilacja do bytecode przyspiesza uruchamianie programów, ponieważ eliminuje konieczność przetwarzania kodu źródłowego za każdym razem.
# Pliki .pyc są przechowywane w katalogu __pycache__ i używane, gdy kod jest uruchamiany ponownie.

# Co oznacza rozszerzenie .pyc?
# Rozszerzenie .pyc oznacza skompilowany plik Pythona (ang. Python Compiled File). Kiedy uruchamiasz program w Pythonie, interpreter Pythona najpierw kompiluje kod źródłowy (plik .py) do postaci bytecode (czyli kodu bajtowego), który jest zapisany w pliku .pyc. Bytecode jest reprezentacją kodu, która może być wykonywana przez Python Virtual Machine (PVM), a nie przez komputer bezpośrednio.
#
# Plik .pyc jest zapisany w katalogu __pycache__ w folderze, w którym znajduje się plik źródłowy .py. Proces kompilacji do bytecode jest wykonywany automatycznie przez Pythona, aby przyspieszyć uruchamianie programu przy kolejnych wykonaniach (wystarczy załadować skompilowany bytecode, zamiast kompilować kod źródłowy za każdym razem).