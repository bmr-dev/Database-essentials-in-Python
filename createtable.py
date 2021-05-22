#!/usr/bin/env python3

# createtable.py
# create a table in SQL Server DB
import pyodbc

# get a connection
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'Trusted_Connection=yes;',
    autocommit = True)

# create SQL script to create table
createTableSQL = ('CREATE TABLE COP2034.dbo.Customer ('
                    'CustomerID varchar(10),'
                    'LastName varchar(255),'
                    'FirstName varchar(255),'
                    'Address varchar(255),'
                    'City varchar(127),'
                    'State varchar(2),'
                    'Zip varchar(9) );')

if conn:
    # create the table
    conn.execute(createTableSQL)
    # close the connection
    conn.close()
else:
    print('Could not get connection!')
