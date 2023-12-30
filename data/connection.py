

import psycopg2

#PostgreSQL database
# Create a new PostgreSQL database connection

def connect_database(  ):
    return psycopg2.connect( database="database_name", user="user_name", password="#####", host="localhost", port="5432" )

