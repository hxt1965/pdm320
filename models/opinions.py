

class Opinion:
    def __init__(self, person_id, question_id, response, database):
        self.person_id = person_id
        self.question_id = question_id
        self.response = response
        self.database = database


    @staticmethod
    def create_table(database):
        query = 'CREATE TABLE IF NOT EXISTS seal18_opinions (' \
                'person_id INTEGER REFERENCES seal18_persons(id), ' \
                'question_id INTEGER REFERENCES seasl18_questions(question_id)),' \
                'response INTEGER DEFAULT 9'
        database.query(query)
        print('Created seal18_opinions table')

    @staticmethod
    def drop_table(database):
        query = 'DROP TABLE IF EXISTS seal18_opinions'
        database.query(query)
        print('Drop seal18_opinions table')

    #@staticmethod
    #def find_by_person_question_id(person_id, question_id, database):
    #    return 

    #run query 
    def save(self):
        query = 'INSERT INTO seal18_opinions (person_id, question_id, response) VALUES (%s, %s, %s)'
        self.database.query(query, (self.person_id, self.question_id, self.response))
        print(query, (self.person_id, self.question_id, self.response))