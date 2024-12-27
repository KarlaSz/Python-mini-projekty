import db
#sesja do polaczen z nasza db
from sqlalchemy.orm import sessionmaker
#losowanie transkacji
import random

#new sessionmaker
Session = sessionmaker(bind=db.engine)
session = Session()

#adding random data
for t in range(10,20):
    item_id = random.randint(0,1000)
    price = random.randint(20,50)
    
    tr.db.tansactions(t, '2020/05/06', item_id, price)
    session.add(tr)
    
#save changes in data base
session.commit()

