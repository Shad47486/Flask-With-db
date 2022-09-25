#import needed modules aKA SQLITE3
import sqlite3

#1 need to connect to sqlite to db
connect = sqlite3.connect('patients.db')

#object db
db = connect.cursor()

#deleting patient_table if it exists
db.execute("DROP TABLE IF EXISTS patient_table")
connect.commit()
# the command "connect.commit()" commits changes done to db
# if command is not ran after work is done it wont save

#need to create a table in the connected database with the command below 
# also need to assign it a var name 
table = """ CREATE TABLE patient_table (
            mrn VARCHAR(255) NOT NULL,
            firstname CHAR(25) NOT NULL,
            lastname CHAR(25) NOT NULL,
            dob CHAR(25) NOT NULL,
            gender CHAR(25) NOT NULL,
            insurance CHAR(25) NOT NULL,
            ssn CHAR(25) NOT NULL,
            phone CHAR(25) NOT NULL
        ); """
# This creates the table in the patients.db file but we need to commit 
# the changes to keep them in the file
db.execute(table)
connect.commit()

#for this assigment we are inserting the example pts to play around work with a fake db
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, gender, insurance, ssn, phone) values('14244', 'David', 'Wine', '01/01/2000', 'M', 'Yes', '222444222', '6316341241')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, gender, insurance, ssn, phone) values('54645', 'Henry', 'Ford', '02/02/2001', 'M', 'No', '213123445', '6316542341')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, gender, insurance, ssn, phone) values('23423', 'Mary', 'Jane', '03/03/2002', 'F', 'No', '768678123', '5160953312')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, gender, insurance, ssn, phone) values('65733', 'Corry', 'William', '04/04/2003', 'M', 'Yes', '345345432', '6315321344')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, gender, insurance, ssn, phone) values('32523', 'Jane', 'Doe', '05/05/2004', 'F', 'No', '456458223', '6315672342')")

# another way to add a patient which may take a little more work is using the commands below (lines 41-42)
#dummyPerson6 = """ INSERT INTO patient_table(mrn, firstname, lastname, dob) values('32323', 'John321', 'Smith123', '01/01/2000') """
#db.execute(dummyPerson6)

connect.commit()


# close the connection
connect.close()