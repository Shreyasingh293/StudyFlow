import mysql.connector

# Creating the connection 'object'
db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="StudyFlow"
)

# This lets other files know the connection is active
if db.is_connected():
    print("✅ System Check: Connection to StudyFlow is Healthy.")
