from database.DB_connect import DBConnect

class DAO():

    @staticmethod
    def getAnni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()

        query = """
           select distinct year(s.`datetime`) as anno
            from new_ufo_sightings.sighting s 
            order by anno asc """

        cursor.execute(query)

        for row in cursor:
            result.append(row[0])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getForme(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()

        query = """
                select distinct s.shape 
                from new_ufo_sightings.sighting s 
                where year(s.`datetime`)=%s """

        cursor.execute(query,(anno,))

        for row in cursor:
            result.append(row[0])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllState():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()

        query = """
                select s.ID
                from new_ufo_sightings.state s  """

        cursor.execute(query)

        for row in cursor:
            result.append((row[0]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArco():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()

        query = """
            select n.*
            from neighbor n 
            where n.state1  < n.state2 
              """

        cursor.execute(query)

        for row in cursor:
            result.append((row[0],row[1]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPeso(stato1,stato2,anno,forma):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()

        query = """
            select count(t.id)
            from(
            select s.state as st1, s2.state as st2 , s2.shape ,s2.id 
            from sighting s , sighting s2 
            where ((s.state=%s and s2.state =%s)or(s2.state=%s and s.state =%s) ) and year(s.`datetime`)=%s and year(s2.`datetime`)=%s and s2.shape =%s and s.shape=%s
            group by s2.id) as t  """

        cursor.execute(query, (stato1,stato2,stato1,stato2,anno,anno,forma,forma))

        for row in cursor:
            result.append(row[0])

        cursor.close()
        conn.close()
        return result

