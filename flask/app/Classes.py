import pymysql.cursors


class DB:
    def __init__(self, server, port, db, user, password, charset):
        self.server = server
        self.port = port
        self.db = db
        self.user = user
        self.password = password
        self.charset = charset

    def q_fetchall(self, query):
        con = pymysql.connect(host=self.server,
                              user=self.user,
                              password=self.password,
                              db=self.db,
                              charset=self.charset,
                              cursorclass=pymysql.cursors.DictCursor)
        cursor = con.cursor()
        cursor.execute(query)
        con.commit()
        ans = cursor.fetchall()
        return ans


db = DB('127.0.0.1', '8000', 'quiz', 'root', 'daniil1999', 'utf8mb4')
