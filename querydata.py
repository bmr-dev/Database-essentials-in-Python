#!/usr/bin/env python3

# querydata.py
# query data from a SQL Server DB
import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'Trusted_Connection=yes;',
    autocommit = True
    )

if conn:
    # get a cursor
    c = conn.cursor()

    #execute the query
    c.execute('SELECT * FROM COP2034.dbo.Customer')

    # loop through the returned data
    while True:
        cust = c.fetchone()
        if cust == None:
            break
        print("Customer:")
        print("\tID:    " + cust[0])
        print("\tLName  " + cust[1])
        print("\tFname  " + cust[2])
        
    conn.close()
