#SQLite - prost baza danych w 1 pliku i jest zawarte w python 3

import sqlite3

#otwieranie bazy danych i nawiazanie polaczenie
db = sqlite3.connect('.simple.db')
cursor = db.cursor()

cursor.execute('''

    CREATE TABLE scores (
      id integer,
      name string,
      surname string,
      score integer)
''')
    
db.commit()
db.close()
