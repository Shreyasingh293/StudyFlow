import dbnewfile # Connects to first file

print("=== SHREYA'S STUDYFLOW LOGGER ===")

# 'cursor' (the hand that writes to the DB)
cursor = dbnewfile.db.cursor()

# Enter inputs
app = input("What app distracted you? ")
mins = input("How many minutes were lost? ")
sub = input("What subject were you doing? ")

# The SQL Command
sql = "INSERT INTO distractions (app_name, duration_minutes, study_subject) VALUES (%s, %s, %s)"
val = (app, mins, sub)

cursor.execute(sql, val)
dbnewfile.db.commit() # "Save" button

print(f"\nSuccessfully logged {mins}m of {app}. Go back to work!")
