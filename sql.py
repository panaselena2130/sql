import sqlite3

db = sqlite3.connect('C:\\Users\Lena\Desktop\magazine.sqlite')

cursor = db.cursor()
query = ''' CREATE TABLE IF NOT EXISTS expenses (id INTEGER, name TEXT) '''
cursor.execute(query)


query1 = ''' INSERT INTO expenses  VALUES(1, 'Komummmmnalka') '''

query2 = ''' INSERT INTO expenses  VALUES(1, 'Komunalka') '''

query3 = ''' INSERT INTO expenses  VALUES(2, 'Benzin') '''

cursor.execute(query1)
cursor.execute(query2)
cursor.execute(query3)
db.commit()







db.close()
