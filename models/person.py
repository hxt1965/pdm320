class Person:
    def __init__(self, response_id, book_count, state, database):
        self.person_id = response_id
        self.book_count = book_count
        self.state = state
        self.database = database

    @staticmethod
    def create_table(database):
        query = 'CREATE TABLE IF NOT EXISTS seal18_persons (person_id PRIMARY KEY, ' \
                'book_count INTEGER DEFAULT 0, state INTEGER) '
        database.query(query)
        print('Create seal18_persons table')

    @staticmethod
    def drop_table(database):
        query = 'DROP TABLE IF EXISTS seal18_persons'
        database.query(query)
        print('Drop seal18_persons table')

    @staticmethod
    def find_by_id(person_id, database):
        query = 'SELECT id, response_id FROM seal18_persons where person_id = (%s)'
        return database.query(query, (person_id,), 'fetchone')

    def save(self):
        query = 'INSERT INTO seal18_persons (response_id, book_count, state) VALUES (%s, %s, %s)'
        self.database.query(query, (self.person_id, self.book_count, self.state))
        print(
            f'Saving a persons with response_id is {self.person_id} and book_count is {self.book_count} to the database')
