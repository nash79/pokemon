import mysql.connector

class DBPokemon(object):
    def __init__(self, login="", basename=""):
        self._connectionlogin=login
        self._connnectiondatabase=basename

    def initdb(self):
        fichier = open("script.sql", "r")
        sql = fichier.read()
        fichier.close()

        cnx = mysql.connector.connect(user="root")
        cursor = cnx.cursor()
        cursor.execute(sql)
        cursor.close()
        cnx.close()

    def callfindalltype(self):
        cnx = mysql.connector.connect(user=self._connectionlogin, database=self._connnectiondatabase)
        cursor = cnx.cursor()
        cursor.callproc('findalltype')
        for r in cursor.stored_results():
            result = r.fetchall()
        cursor.close()
        cnx.close()
        return result

    def callinserttype(self, designationtype):
        cnx = mysql.connector.connect(user=self._connectionlogin, database=self._connnectiondatabase)
        cursor = cnx.cursor()
        arg =[]
        arg.append(designationtype)
        arg.append('')
        result = cursor.callproc('inserttype', arg)
        cursor.close()
        cnx.commit()
        cnx.close()
        return result[-1]

    def callupdatetype(self, olddesignationtype, newdesignationtype):
        cnx = mysql.connector.connect(user=self._connectionlogin, database=self._connnectiondatabase)
        cursor = cnx.cursor()
        arg = []
        arg.append(olddesignationtype)
        arg.append(newdesignationtype)
        arg.append('')
        result = cursor.callproc('updatetype', arg)
        cursor.close()
        cnx.commit()
        cnx.close()
        return result[-1]

    def calldeletetype(self, designationtype):
        cnx = mysql.connector.connect(user=self._connectionlogin, database=self._connnectiondatabase)
        cursor = cnx.cursor()
        arg = []
        arg.append(designationtype)
        cursor.callproc('deletetype', arg)
        cursor.close()
        cnx.commit()
        cnx.close()




    def callfindallpokemon(self):
        cnx = mysql.connector.connect(user=self._connectionlogin, database=self._connnectiondatabase)
        cursor = cnx.cursor()
        cursor.callproc('findallpokemon')
        for r in cursor.stored_results():
           result = r.fetchall()
        cursor.close()
        cnx.close()
        return result

    def callinsertpokemon(self, nompokemon):
        cnx = mysql.connector.connect(user=self._connectionlogin, database=self._connnectiondatabase)
        cursor = cnx.cursor()
        arg =[]
        arg.append(nompokemon)
        arg.append('')
        result = cursor.callproc('insertpokemon', arg)
        cursor.close()
        cnx.commit()
        cnx.close()
        return result[-1]

    def callupdatepokemon(self, nompokemon, nouveaunompokemon):
        cnx = mysql.connector.connect(user=self._connectionlogin, database=self._connnectiondatabase)
        cursor = cnx.cursor()
        arg = []
        arg.append(nompokemon)
        arg.append(nouveaunompokemon)
        arg.append('')
        result = cursor.callproc('updatepokemon', arg)
        cursor.close()
        cnx.commit()
        cnx.close()
        return result[-1]

    def calldeletepokemon(self, nompokemon):
        cnx = mysql.connector.connect(user=self._connectionlogin, database=self._connnectiondatabase)
        cursor = cnx.cursor()
        arg = []
        arg.append(nompokemon)
        cursor.callproc('deletepokemon', arg)
        cursor.close()
        cnx.commit()
        cnx.close()




    def callfindfeature(self, nompokemon):
        cnx = mysql.connector.connect(user=self._connectionlogin, database=self._connnectiondatabase)
        cursor = cnx.cursor()
        arg = []
        arg.append(nompokemon)
        cursor.callproc('findfeature', arg)
        for r in cursor.stored_results():
            result = r.fetchall()
        cursor.close()
        cnx.close()
        return result

    def callinsertfeature(self, nompokemon, designationtransformation, designationtype1, designationtype2, paramhp, paramattack, paramdefense, paramspeed_Attack, paramspeed_Defense, paramspeed):
        cnx = mysql.connector.connect(user=self._connectionlogin, database=self._connnectiondatabase)
        cursor = cnx.cursor()
        arg =[]
        arg.append(nompokemon)
        arg.append(designationtransformation)
        arg.append(designationtype1)
        arg.append(designationtype2)
        arg.append(paramhp)
        arg.append(paramattack)
        arg.append(paramdefense)
        arg.append(paramspeed_Attack)
        arg.append(paramspeed_Defense)
        arg.append(paramspeed)
        arg.append('')
        result = cursor.callproc('insertfeature', arg)
        cursor.close()
        cnx.commit()
        cnx.close()
        return result[-1]

    def callupdatefeature(self, nompokemon, designationtransformation, designationtype1, designationtype2, paramhp, paramattack, paramdefense, paramspeed_Attack, paramspeed_Defense, paramspeed):
        cnx = mysql.connector.connect(user=self._connectionlogin, database=self._connnectiondatabase)
        cursor = cnx.cursor()
        arg = []
        arg.append(nompokemon)
        arg.append(designationtransformation)
        arg.append(designationtype1)
        arg.append(designationtype2)
        arg.append(paramhp)
        arg.append(paramattack)
        arg.append(paramdefense)
        arg.append(paramspeed_Attack)
        arg.append(paramspeed_Defense)
        arg.append(paramspeed)
        arg.append('')
        result = cursor.callproc('updatefeature', arg)
        cursor.close()
        cnx.commit()
        cnx.close()
        return result[-1]

    def calldeletefeature(self, nompokemon, designationtransformation, designationtype1, designationtype2):
        cnx = mysql.connector.connect(user=self._connectionlogin, database=self._connnectiondatabase)
        cursor = cnx.cursor()
        arg = []
        arg.append(nompokemon)
        arg.append(designationtransformation)
        arg.append(designationtype1)
        arg.append(designationtype2)
        cursor.callproc('deletefeature', arg)
        cursor.close()
        cnx.commit()
        cnx.close()