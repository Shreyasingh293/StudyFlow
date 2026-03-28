import dbnewfile

cursor = dbnewfile.db.cursor()

print("🛠️ STUDYFLOW MANAGER")
print("1. Search distractions by Subject")
print("2. Delete a specific log (by ID)")

choice = input("\nSelect an option (1 or 2): ")

if choice == "1":
    sub = input("Enter subject name (e.g., Physics): ")
    query = "SELECT app_name, duration_minutes, time_stamp FROM distractions WHERE study_subject = %s"
    cursor.execute(query, (sub,))
    
    results = cursor.fetchall()
    print(f"\n--- Logs for {sub} ---")
    for row in results:
        print(f"App: {row[0]} | Mins: {row[1]} | Date: {row[2]}")

elif choice == "2":
    # First, show the IDs which is to be deleted
    cursor.execute("SELECT id, app_name, study_subject FROM distractions")
    for row in cursor.fetchall():
        print(f"ID: {row[0]} | {row[1]} during {row[2]}")
        
    target_id = input("\nEnter the ID number to delete: ")
    cursor.execute("DELETE FROM distractions WHERE id = %s", (target_id,))
    dbnewfile.db.commit()
    print(f"Successfully deleted entry ID {target_id}.")

else:
    print("Invalid choice!")
