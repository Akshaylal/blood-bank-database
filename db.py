import mysql.connector

DATABASE='BloodBankDB'

class BBDB:
    def __init__(self, host, user, password):
        self.connectDB(host, user, password)
        mycursor = self.db.cursor()
    
    def connectDB(self, host, user, password):
        try:
            self.db = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=DATABASE
            )
            self.status = 'Connected'
        except mysql.connector.Error as err:
            print(err)
            if err.errno == 2003:
                self.status = 'Cannot conect to server {host}'
            elif err.errno == 1698:
                self.status = 'Access denied'
            elif err.errno == 1049:
                initDB()
        except:
            self.status = f'Something Went Wrong: {err}'
        print(self.status)
    
    def initDB(self):
        mycursor = self.db.cursor()
        mycursor.execute(f'CREATE DATABASE {DATABASE}')

if __name__ == '__main__':
    x=BBDB('localhost', 'bloodbank', 'bloodbank')
