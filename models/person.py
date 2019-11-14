class Person:
    def __init__(self, response_id, book_count, database):
        self.response_id = response_id
        self.book_count = book_count
        self.database = database

    @staticmethod
    def create_table(database):
        query = 'CREATE TABLE IF NOT EXISTS persons (id SERIAL PRIMARY KEY, response_id INTEGER UNIQUE, book_count ' \
                'INTEGER DEFAULT 0)'
        database.query(query)
        print('Create persons table')

    @staticmethod
    def drop_table(database):
        query = 'DROP TABLE IF EXISTS persons'
        database.query(query)
        print('Drop persons table')

    @staticmethod
    def find_by_response_id(response_id, database):
        query = 'SELECT id, response_id FROM persons where response_id = (%s)'
        return database.query(query, (response_id,), 'fetchone')

    def save(self):
        query = 'INSERT INTO persons (response_id, book_count) VALUES (%s, %s)'
        self.database.query(query, (self.response_id, self.book_count))
        print(
            f'Saving a persons with response_id is {self.response_id} and book_count is {self.book_count} to the database')
