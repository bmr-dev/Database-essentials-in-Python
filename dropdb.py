#!/usr/bin/env python3

# dropdb.py
# drop a SQL Server DB
import pyodbc

# get a connection
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'Trusted_Connection=yes;',
    autocommit = True
    )

if conn:    
    # drop the database
    conn.execute('DROP DATABASE COP2034')
    # close the connection
    conn.close()
else:
    print('could not get connection!')
