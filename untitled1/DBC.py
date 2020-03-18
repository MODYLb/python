import shelve


db = shelve.open('db')
for i in db.keys():
    print(db[i])

db.close()