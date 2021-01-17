import mysql.connector

DATABASE='BloodBankDB'

class BBDB:
    def __init__(self):
        pass
    
    def connectDB(self):
        pass
    
    def initDB(self):
        pass

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host='localhost',
        user='bloodbank',
        password='bloodbank'
    )
    print(mydb)
    mycursor = mydb.cursor()
    mycursor.execute('SHOW DATABASES')
    for x in mycursor:
        print(x)
