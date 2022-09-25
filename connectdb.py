#import needed modules 
import pandas as pd 
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('patients.db')
    conn.row_factory = sqlite3.Row
    return conn

#getting the connection to database in line 12 
#line 14 is using a sql command to grab
#all the data from that table and giving it a var name of 'patientlistSql'
db = get_db_connection()
patientListSql = db.execute('SELECT * FROM patient_table').fetchall()
patientListSql

# saves the data to a dataframe using pandas
df = pd.DataFrame(patientListSql)
df

# renames the columns to the names given in the orginal file
df.columns = ['mrn', 'firstname', 'lastname', 'dob', 'gender', 'insurance', 'ssn', 'phone']
df