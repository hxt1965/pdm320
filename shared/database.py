import psycopg2
import psycopg2.extras


class Database(object):
    def __init__(self):
        self._connection = psycopg2.connect(
            host='reddwarf.cs.rit.edu',
            dbname='p32003f',
            user='p32003f',
            password='ahpohsaejaeph3Die7ez',
            port='5432'
        )
        self._cur = self._connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def query(self, query, params=None, method=None):
        if params is None:
            self._cur.execute(query)
        self._cur.execute(query, params)

        if (method is None):
            return self._connection.commit()
        elif (method == 'fetchone'):
            return self._cur.fetchone()
        return self._cur.fetchall()

    def __del__(self):
        self._connection.close()
        self._cur.close()
