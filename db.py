import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_tkinter"

)
cursor_ = db.cursor()


def check(user,passw,cursor_):
    cursor_.execute("SELECT id FROM db WHERE username = %s AND password = %s LIMIT 1", (user, passw))
    result = cursor_.fetchone()

    if result:
      user_id = result[0]
      return user_id
    
    return None
