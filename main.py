import sqlite3

c = sqlite3.connect("Mr.Programmer.db")
cu = c.cursor()


sql_command = """CREATE TABLE IF NOT EXISTS krish (sno INTEGER PRIMARY KEY,name VARCHAR(30));"""
cu.execute(sql_command)

for i in range(1,10):
    sql_command = """INSERT INTO krish VALUES ("""+str(i)+""", "krishna");"""
    cu.execute(sql_command)

cu.execute("SELECT * FROM krish")

print(cu.fetchall())


c.close()
