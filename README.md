# StudyFlow: Mobile-First Productivity Tracker 🚀

A full-stack Python application developed entirely on Android to track and analyze study distractions during Boards and Competetive exams or any other preparation.

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

## 🚀 How to Run Step-by-Step Setup Guide (Android)
​Follow these steps exactly to get StudyFlow running on your device.
​1. Install the Essentials
​Download these two apps from the Play Store:
​Pydroid 3: For running the Python code.
​Termux: For hosting the MariaDB database.

​2. Prepare the Python Environment (Pydroid 3)
​Open Pydroid 3, go to the Pip menu, and install the database connector:
mysql-connector-python

3. Setup the Database (Termux)
​Open Termux and run these commands one by one:
I)Install MariaDB: pkg install mariadb
II)Start the Server: mysqld_safe -u root &
III)Enter SQL: mariadb -u root
IV)Create the Project Space:

CREATE DATABASE StudyFlow;
USE StudyFlow;

CREATE TABLE distractions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    app_name VARCHAR(255),
    duration INT,
    subject VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

4. Run `logger.py` in Pydroid 3 to log a session.
5. Run `analyzer.py` to see your biggest "Distraction Enemy."

​🛠️ Common Troubleshooting (The "Error 2002" Fix)
​If you see ERROR 2002 (HY000): Can't connect to local server, it means the database server is sleeping. 
The Fix: Go to Termux and type mysqld_safe -u root &. Wait 10 seconds, and try again!
