import mysql.connector
#connect to db
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_tkinter"

)
cursor_ = db.cursor()

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