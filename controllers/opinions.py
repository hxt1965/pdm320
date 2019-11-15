import pandas

from models.opinions import Opinion
from models.questions import Question

class OpinionController:

    op_list = ['eminuse', 'intmob', 'intfreq', 'pial5a', 'pial5b', 'pial5c', 'pial5d',
                'pial11', 'pial11a', 'pial12', 'books1', 'books2a',
                'books2b', 'books2c']

    def __init__(self, file_name, database):
        self.df = pandas.read_csv(file_name)
        self.rows = self.df.shape[0]
        self.database = database

    def init_table_values(self):
        Opinion.drop_table(self.database)
        Opinion.create_table(self.database)

        for i in range(1, 2002):
            q_num = 1
            for col in op_list:
                person_id = int(i)
                if i in df.respid:
                    op = Opinion(person_id, q_num, int(df[col][i]), self.database)
                    op.save()
                q_num = q_num + 1

