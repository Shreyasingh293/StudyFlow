# StudyFlow: Mobile-First Productivity Tracker 🚀

A full-stack Python application developed entirely on Android to track and analyze study distractions during CBSE Class 10, Class 12 board ,Competetive exams Or any other academic preparation.

## 🌟 The "Shreya" Perspective
Preparing for competitive exams like WBJEE,CUET and IIIT-H requires intense focus. I built this tool to move from "feeling" distracted to "measuring" distractions using data science principles.

## 🛠️ Tech Stack
- **Language:** Python 3.11 (via Pydroid 3)
- **Database:** MariaDB/MySQL (via Termux)
- **Environment:** Android (Mobile-only development)

## 🏗️ System Architecture
The project follows a modular "3-Tier" architecture:
1. **dbnewfile.py**: Database abstraction layer (The Pipe).
2. **logger.py**: Secure data entry with input validation (The Input).
3. **analyzer.py**: SQL-based data analytics engine (The Intelligence).
4. **manager.py**: CRUD operations for data maintenance (The Control).

## 📊 Features
- **Automatic Timestamps**: Uses SQL `CURRENT_TIMESTAMP` for time-series data.
- **Error Handling**: Graceful degradation if the database server is offline.
- **Input Validation**: Prevents "dirty data" (negative minutes or empty entries).
- **Subject-Specific Analytics**: Filters distractions by subject (Physics, Chemistry, Maths).

## 🚀 How to Run
1. Start MariaDB in Termux: `mysqld_safe -u root &`
2. Create the `StudyFlow` database and `distractions` table in SQL.
3. Run `logger.py` in Pydroid 3 to log a session.
4. Run `analyzer.py` to see your biggest "Distraction Enemy."
