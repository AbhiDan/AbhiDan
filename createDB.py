import sqlite3
import pandas as pd
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    conn.commit()
    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_task_by_priority(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM projects")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def create_table(conn,create_sql_table):
    try:
        cur = conn.cursor()
        #cur.execute("DROP TABLE projects")
        #conn.commit()
        cur.execute(create_sql_table)
        conn.commit()
    except Error as e:
        print(e)


def add_table_entry(conn,data_entry):
    try:
        cur = conn.cursor()
        cur.executemany("""INSERT or REPLACE INTO users values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);""",data_entry);
        conn.commit()
    except Error as e:
        print(e)
        
def convert_to_dataframe(conn):
    dfprojects = pd.read_sql_query("SELECT * from users", conn)
    return dfprojects
    
def select_row_with_patient_id(conn,dfprojects,patient_id):
    row = dfprojects.loc[dfprojects['Patient_id']== patient_id]
    return row
    
def append_a_row(conn,dfprojects,newrowentry):
    newdf = pd.DataFrame(dfprojects)
    newdf = newdf.append(newrowentry,ignore_index=True)
    print (newdf)

def main():
    #database = r"C:\sqlite\db\pythonsqlite.db"
    database = r"c:\sqlite\db\USER_ACCOUNT_DB.db"
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                    Patient_id integer PRIMARY KEY,
                                    Patient_name text NOT NULL,
                                    DOB text,
                                    City text
                                    ); 
                                """
    '''
    data_entry = [(1,'Osler1','29/10/2021','Staines'),
                  (2,'Osler2','31/10/2021','Oxford'),
                  (3,'Osler3','02/10/2021','London'),
                  (4,'Osler4','04/10/2021','Cambridge'),
                  (5,'Osler5','31/10/2021','Bath'),
                  (6,'Osler6','02/10/2021','Bristol'),
                  (7,'Osler7','29/10/2021','Cardiff'),
                  (8,'Osler8','31/10/2021','Galsgow'),
                  (9,'Osler9','02/10/2021','Southampton'),
                  (10,'Osler10','29/10/2021','Bournemouth'),
                  (11,'Osler11','31/10/2021','Yorkshire'),
                  (12,'Osler12','02/10/2021','Lecister')
                 ]
    '''
    data_entry = [(2, '', None, 'adandade', 'Password2', None, None, 1, 1, 1, 0, 0, 0, 1635917748341, 1635917748341, 1635917748341, '')]
    # create a database connection
    conn = create_connection(database)
    '''
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)
    else:
        print("Error! cannot create the database connection.")
        
    add_table_entry(conn,data_entry)
    '''
           
    with conn:
    #    print("1. Query task by priority:")
    #    select_task_by_priority(conn)
    #    print("2. Query all tasks")
         add_table_entry(conn,data_entry)
         select_all_tasks(conn)
    #     db_in_df = convert_to_dataframe(conn)
    #     print(db_in_df)
        # print("Selected row from the table")
        # row = select_row_with_patient_id(conn,db_in_df,10)
        # print(row)
        # newentry = {'Patient_id':13,'Patient_name':'Osler13','DOB':'05/09/2021','City':'Ashford'}
        # append_a_row(conn,db_in_df,newentry)
         
    
    #cur = conn.cursor()
    #cur.execute("DROP TABLE users")
    conn.close()


if __name__ == '__main__':
    main()