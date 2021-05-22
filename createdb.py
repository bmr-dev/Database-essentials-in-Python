#!/usr/bin/env python3

# createdb.py
# create a SQL Server DB
import pyodbc

# get a connection
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'Trusted_Connection=yes;',  # use Windows Authentication
    autocommit = True
    )

if conn:    
    # create the database
    conn.execute('CREATE DATABASE COP2034')
    # turn off auto-close so DB isn't taken offline
    # (this is SQL Server-specific)
    conn.execute('ALTER DATABASE COP2034 SET AUTO_CLOSE OFF')
    conn.close()
else:
    print('could not get connection!')
