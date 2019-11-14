self.questions = ['eminuse', 'intmob', 'intfreq', 'pial5a', 'pial5b', 'pial5c', 'pial5d',
                'pial11', 'pial11a', 'pial12', 'books1', 'books2a',
                'books2b', 'books2c']

class Question: 
    def __init__(self, question_id, question_attr, database):
        self.question_id = question_id
        self.question_attr = question_attr
        self.database = database

    @staticmethod
    def create_table(database):
        query = 'CREATE TABLE IF NOT EXISTS seal18_questions (' \
                'question_id INTEGER PRIMARY KEY,' \
                'question_attr VARCHAR(20) NOT NULL'
        database.query(query)
        print('Created seal18_questions table')

    @staticmethod
    def drop_table(database):
        query = 'DROP TABLE IF EXISTS seal18_questions'
        database.query(query)
        print('Dropped seal18_questions table')

    def save(self):
        query = 'INSERT INTO seal18_questions (question_id, question_attr)'
        self.database.query(query, (self.question_id, self.question_attr))
        print('Saved question ', self.question_attr)

    #Return question instance to opinions 
    def find_by_question_attr(self, question_str):
        query = 'SELECT question_id FROM seal18_questions'
        return 