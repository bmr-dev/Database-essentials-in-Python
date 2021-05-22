#!/usr/bin/env python3

# droptable.py
# drop a table in SQL Server DB
import pyodbc

# get a connection
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'Trusted_Connection=yes;',
    autocommit = True)

# create SQL script to drop table
dropTableSQL = 'DROP TABLE COP2034.dbo.Customer'

if conn:
    conn.execute(dropTableSQL)
    # close the connection
    conn.close()
else:
    print('Could not get connection!')
