#!/usr/bin/env python3

# createdata.py
# insert rows into a table in a SQL Server DB
import pyodbc

# get a connection
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'Trusted_Connection=yes;',
    autocommit = True)

# create SQL script to insert a row
insertRow1SQL = "INSERT INTO COP2034.dbo.Customer VALUES ('A10001', 'Smith', 'John', '1 Elm St.,', 'Jacksonville', 'FL', '32242')"
insertRow2SQL = "INSERT INTO COP2034.dbo.Customer VALUES ('B10002', 'Brown', 'Sally', '3 Oak St.,', 'Orlando', 'FL', '32806')"

if conn:
    # create the table
    conn.execute(insertRow1SQL)
    conn.execute(insertRow2SQL)
    # close the connection
    conn.close()
else:
    print('Could not get connection!')
