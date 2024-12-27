import sqlite3


db = sqlite3.connect("simple.db")
cursor = db.cursor()

cursor.execute('''
 insert into scores (id,name,surname,score) values (1,"Jack", "Black", 76)
''')

db.commit()
db.close()
