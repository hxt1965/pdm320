import demographics as dem
import devices as dev
import opinions as op
import social_media as soc
import person as per
import psycopg2 
import subprocess


def main():
    op.main('trends.csv')
    dem.main('trends.csv')
    soc.main('trends.csv')
    dev.main('trends.csv')
    per.main('trends.csv')
    return 

if __name__ =='__main__':
    main()

class db(object):
    def __init__(self):
        self._connection = psycopg2.connect(
                        host = 'reddwarf.cs.rit.edu',
                        dbname = 'postgres',
                        user = 'p32003f',
                        password = 'ahpohsaejaeph3Die7ez',
                        port = '5432'
                    )
        self._cur = self._connection.cursor()

    def query(self, query, params):
        return self._cur.execute(query, params)

    def __del__(self):
        self._connection.close()
