import pyodbc
import os
# Some other example server values are
if os.name == 'nt':
    server = 'localhost\sqlexpress'  # for a named instance
else:
    server = 'localhost'
# server = 'myserver,port' # to specify an alternate port
# server = 'tcp:myserver.database.windows.net'
database = 'ems_db'
username = 'sa'
password = 'Born19861216'
if os.name == 'nt':
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                          server + ';DATABASE=' + database +
                          ';Trusted_Connection=yes')
else:
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                          server + ';DATABASE=' + database + ';UID=' +
                          username + ';PWD=' + password)
cursor = cnxn.cursor()

cursor.execute("SELECT @@version;")
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()
