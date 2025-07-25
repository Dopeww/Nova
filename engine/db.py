import sqlite3

con = sqlite3.connect("nova.db")
cursor = con.cursor()

#####  TABLE QUERY  #####
query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

query = "INSERT INTO sys_command VALUES (null,'', '')"
cursor.execute(query)
con.commit()