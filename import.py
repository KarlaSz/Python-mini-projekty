#porownujemy zmienna z main,
#name to spejclana zmienna ktora PY przydzile naszym plikom ktore bedziemy uruchamiac zanim przetworzymy kod
#uzywane przy importach przy kilku plikach
#za kazdym razem gdy importujemy cos z innego pliku, bo inaczej odpali sie kod z tego importowanego pliku niepotrzebnie
#najpierw wykonuje sie kod z pliku importowanego,a pozniej w pliku oryginalnym

def hello():
    print('testuje')

if __name__ == '__main__':
    hello()
    hello()
    hello()
    hello()
    hello()
    hello()
    
    
    
    
    ###
    #wdrugim pliku
    
    import file1
    
    file1.hello()
