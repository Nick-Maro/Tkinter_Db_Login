import mysql.connector

# Replace with your actual credentials
hostname = "sql7.freesqldatabase.com"
database = "sql7721681"
username = "sql7721681"
password = "zrPv6w65lL"
port = 3306

try:
    db = mysql.connector.connect(
        host=hostname,
        database=database,
        user=username,
        password=password,
        port=port
    )

    print("Connection established successfully!")

except mysql.connector.Error as err:
    print("Connection failed:", err)



cursor_ = db.cursor()
cursor2_ = db.cursor()
def tree(columns=None):
    query = "SELECT " + (", ".join(columns) if columns else "*") + " FROM db"
    try:
        cursor2_.execute(query)
        result = cursor2_.fetchall()
        return result
    except mysql.connector.Error as err:
        print("Database query error:", err)
        return None  # Or handle the error differently
 
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
        #logging.info(f"User with ID {index} deleted successfully")
        return True
    except Exception as e:
        #logging.error(f"Error deleting user with ID {index}: {e}")
        return False
def add(username,password):
    sql = "INSERT INTO db (username, password) VALUES (%s, %s)"
    valori = (username, password)
    cursor_.execute(sql,valori)
    db.commit()
#def change_password(old_password,id):
#    sql = ""