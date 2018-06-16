import mysql.connector

cnx = mysql.connector.connect(user="root", database="pokemon")
cursor = cnx.cursor()
arg =[]
arg.append("test1")
arg.append("")
arg_result = cursor.callproc('inserttype', arg)
print(arg_result[-1])
for r in cursor.stored_results():
    print(r.fetchall())
cursor.close()
cnx.commit()
cnx.close()