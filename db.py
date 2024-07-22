import mysql.connector
import logging
#connect to db
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_tkinter"

)
cursor_ = db.cursor()
cursor2_ = db.cursor()
def tree():
  cursor2_.execute("SELECT * FROM db")
  result = cursor2_.fetchall()
  return result
#searching id which username and password match
def check(user, password, cursor_):
    try:
        cursor_.execute("SELECT id, Privileges FROM db WHERE username = %s AND password = %s LIMIT 1", (user, password))
        result = cursor_.fetchone()

        if result:
            return list(result)  
        else:
            return None

    except Exception as e:
        #error
        print(f"Error: {e}")
        return None
    
def delete(index):
    try:
        cursor_.execute("DELETE FROM db WHERE id = %s", (index,))
        db.commit()
        logging.info(f"User with ID {index} deleted successfully")
        return True
    except Exception as e:
        logging.error(f"Error deleting user with ID {index}: {e}")
        return False
def add(username,password):
    sql = "INSERT INTO db (username, password) VALUES (%s, %s)"
    valori = (username, password)
    cursor_.execute(sql,valori)
    db.commit()