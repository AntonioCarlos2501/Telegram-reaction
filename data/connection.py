

import psycopg2

#PostgreSQL database
# Create a new PostgreSQL database connection

#Create a database 
#Insert a new table into the database with the columns 'group_name', 'idgroup', 'username', 'userid', 'reaction_type'

def connect_database(  ):
    return psycopg2.connect( database="database_name", user="user_name", password="#####", host="localhost", port="5432" )

