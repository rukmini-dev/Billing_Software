
Billing Software Project
A simple desktop application built with Python and Tkinter to manage billing in a retail store. The application stores billing data in a MySQL database and uses Pillow to display an image/logo.

🧾 Requirements
Python 3.x
Download and install from: https://www.python.org/downloads

Python Libraries
Install via pip:

bash
Copy
Edit
pip install pillow mysql-connector-python
pillow — For displaying logo images

mysql-connector-python — For connecting Python to MySQL

MySQL Server

Username: root

Password: '' (blank)

⚠️ If your MySQL password is different, update it in billing_app.py

📁 Project Files
**billing_app.py** – The main GUI application built with Tkinter

**logo.png** – Logo image displayed in the app interface

**setup_database.sql** – SQL script to create the required MySQL database and tables

▶️ Running the App
Set up the database

Open MySQL CLI or MySQL Workbench

Run the script:

sql
Copy
Edit
source setup_database.sql;
Prepare files

Make sure billing_app.py and logo.png are in the same folder

Launch the application

Run from terminal or command prompt:

bash
Copy
Edit
python billing_app.py
