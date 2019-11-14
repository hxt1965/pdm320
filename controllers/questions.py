import pandas

from models.questions import Question

op_list = ['eminuse', 'intmob', 'intfreq', 'pial5a', 'pial5b', 'pial5c', 'pial5d',
                'pial11', 'pial11a', 'pial12', 'books1', 'books2a',
                'books2b', 'books2c']

class QuestionsController:
    def __init__(self, file_name, database):
        self.df = pandas.read_csv(file_name)
        self.rows = self.df.shape[0]
        self.database = database

    def init_table_values(self):
        Question.drop_table(self.database)
        Question.create_table(self.database)

        for i in range(len(op_list)):
            q_obj = Question(i+1, op_list[i], self.database)
            q_obj.save()
