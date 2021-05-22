#!/usr/bin/env python3

#Bryan Ricardo
#Working with Databases

import pyodbc

#Method to create data
def create_data(conn):
    
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


#Method to create database
def create_db(conn):
    if conn:    
        # create the database
        conn.execute('CREATE DATABASE COP2034')
        # turn off auto-close so DB isn't taken offline
        # (this is SQL Server-specific)
        conn.execute('ALTER DATABASE COP2034 SET AUTO_CLOSE OFF')
        conn.close()
    else:
        print('could not get connection!')

#method to create table
def create_table(conn):
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


#Method to delete data
def delete_data(conn):
    # create SQL script to delete all rows
    deleteRow1SQL = 'DELETE FROM COP2034.dbo.Customer'

    if conn:
        # delete the rows
        conn.execute(deleteRow1SQL)
        # close the connection
        conn.close()
    else:
        print('Could not get connection!')


#Method to drop database
def drop_db(conn):
    if conn:    
        # drop the database
        conn.execute('DROP DATABASE COP2034')
        # close the connection
        conn.close()
    else:
        print('could not get connection!')


#Method to drop table
def drop_table(conn):
    # create SQL script to drop table
    dropTableSQL = 'DROP TABLE COP2034.dbo.Customer'

    if conn:
        conn.execute(dropTableSQL)
        # close the connection
        conn.close()
    else:
        print('Could not get connection!')


#Method to query data
def query_data(conn):
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




def main():
    # get a connection
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'Trusted_Connection=yes;',  # use Windows Authentication
        autocommit = True
        )

    #call methods here
    create_db(conn)

    create_table(conn)

    create_data(conn)

    query_data(conn)

    delete_data(conn)

    drop_table(conn)

    drop_db(conn)



#call the main function with top level scope check
if __name__ == "__main__":
    main()