import mysql.connector
db = mysql.connector.connect(host="localhost", username="root", password="Kite@2021", database="persons")
cursor = db.cursor()
file = open(r"C:\Users\Viji\OneDrive\Documents\file.txt")
data = []
while True:
    content = file.readline()
    if not content:
        break
    res = content.split()
    data.append(res)
    print(data)
file.close()
query = "INSERT INTO colls(`namess`,`phonenumber`,`email`,`city`) VALUES(%s,%d,%s,%s)"
cursor.executemany(query, data)
db.commit()
cursor.close()
print('done')







