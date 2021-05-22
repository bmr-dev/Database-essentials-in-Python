#!/usr/bin/env python3

# deletedata.py
# delete rows from a table in a SQL Server DB
import pyodbc

# get a connection
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'Trusted_Connection=yes;',
    autocommit = True)

# create SQL script to delete all rows
deleteRow1SQL = 'DELETE FROM COP2034.dbo.Customer'

if conn:
    # delete the rows
    conn.execute(deleteRow1SQL)
    # close the connection
    conn.close()
else:
    print('Could not get connection!')
