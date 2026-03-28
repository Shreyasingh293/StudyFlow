import dbnewfile

cursor = dbnewfile.db.cursor()

print("📊 STUDYFLOW WEEKLY ANALYSIS")

# 1.Total Minutes Wasted:-
cursor.execute("SELECT SUM(duration_minutes) FROM distractions")
total = cursor.fetchone()[0] or 0

# 2.Biggest Distracting Enemy (The most used app)
cursor.execute("SELECT app_name, SUM(duration_minutes) as total FROM distractions GROUP BY app_name ORDER BY total DESC LIMIT 1")
enemy = cursor.fetchone()

print(f"Total time lost this week: {total} minutes")

if enemy:
    print(f"Biggest Distraction: {enemy[0]} ({enemy[1]} mins)")

# 3. Motivation giving code 
if total > 120:
    print("\n⚠️ WARNING: You've lost 2+ hours. Physics prep is at risk!")
else:
    print("\n✅ GREAT JOB: You are staying disciplined.")
