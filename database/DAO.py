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