import sqlite3
import random
from os import name

try:
    db = sqlite3.connect('.simple.db')
    cursor = db.cursor()
    print("DB open")
    
    names = ["Mikel", "Tom", "Bart", "Ann"]
    sunames = ["Davis", "Johnons", "Nowak", "Kowalik"]
    id = 0 
    
    for _ in range(20):
        name = random.choice(names)
        surname = random.choice(surnames)
        result = random.randint(0,100)
        
        print(name, surname, result)
        
        cursor.execute(f''' 
            insert into scores (id, name, surname, score) values (
            {id}, "{name}", "{surname}", {result})
            ''')
            
        id += 1
    print("Done")
    
    db.commit()
    db.close()
except:
    print("fail")
