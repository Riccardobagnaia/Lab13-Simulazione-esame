from database.DB_connect import DBConnect

class DAO():

    @staticmethod
    def getAnni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()

        query = """
               select distinct year(s.`datetime` )
                from sighting s """

        cursor.execute(query)

        for row in cursor:
            result.append(row[0])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAvvistamenti(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()

        query = """
            select count(*)
            from sighting s 
            where year(s.`datetime`)=%s """

        cursor.execute(query,(anno,))

        for row in cursor:
            result.append(row[0])

        cursor.close()
        conn.close()
        return result



    @staticmethod
    def getNodi(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()

        query = """
            select distinct s.state
            from sighting s
            where year(s.`datetime`)= %s """

        cursor.execute(query, (anno,))

        for row in cursor:
            result.append(row[0])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArco(stato1, stato2):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)

        query = """
                select sA.state as stato1, sB.state as stato2
                from sighting sA , sighting sB
                where sA.`datetime` < sB.`datetime` and sA.state=%s and sB.state=%s
                limit 1 """

        cursor.execute(query, (stato1, stato2))

        for row in cursor:
            result.append((row["stato1"], row["stato2"]))

        cursor.close()
        conn.close()
        return result


