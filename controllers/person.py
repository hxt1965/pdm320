import pandas

from models.person import Person


class PersonController:

    def __init__(self, file_name, database):
        self.df = pandas.read_csv(file_name)
        self.rows = self.df.shape[0]
        self.database = database

    def init_table_values(self):
        Person.drop_table(self.database)
        Person.create_table(self.database)

        for i in range(self.rows):
            response_id = int(self.df['respid'][i])
            book_count = int(self.df['books1'][i])
            state = int(self.df['state'][i])
            person = Person(response_id, book_count, state, self.database)
            person.save()

    def find(self, response_id):
        return Person.find_by_id(response_id, self.database)
