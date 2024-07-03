from database.DB_connect import DBConnect

class DAO():

    @staticmethod
    def getStati():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()

        query = """
            select distinct(s.id)
            from state s"""

        cursor.execute(query)

        for row in cursor:
            result.append(row[0])

        cursor.close()
        conn.close()
        return result



    @staticmethod
    def getArchi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()

        query = """
            select n.state1 , n.state2 
            from neighbor n 
            where n.state1  < n.state2 """

        cursor.execute(query)

        for row in cursor:
            result.append((row[0],row[1]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPeso(stato1,stato2,data,xG):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()

        query = """
            select count(t.id) as peso
            from(
            select  s.state as stato1, s2.state as stato2, s2.`datetime` as giorni , s2.id 
            from sighting s , sighting s2  
            where year(s2.`datetime`) = %s and year(s.`datetime`) = %s and ((datediff(s2.`datetime`,s.`datetime`)<%s and datediff(s2.`datetime`,s.`datetime`)>0)or(datediff(s.`datetime`,s2.`datetime`)<%s 
            and datediff(s.`datetime`,s2.`datetime`)>0 )) and s2.state != s.state and ((s.state=%s and s2.state =%s)or(s2.state=%s and s.state =%s))
            group by s2.id ) as t """

        cursor.execute(query,(data,data,xG,xG,stato1,stato2,stato1,stato2))

        for row in cursor:
            result.append(row[0])

        cursor.close()
        conn.close()
        return result