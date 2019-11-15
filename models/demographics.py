class Demographics:
    def __init__(self, database, respid, info):
        self.respid = respid
        self.db = database
        self.info = {k: v for k, v in info.items() if v is not None}

    @staticmethod
    def create_table(db):
        query = ("CREATE TABLE seal18_demographics("
                 "person_id int NOT NULL, sex int, age int, "
                 "maritalStatus int, education int, employment int, "
                 "race int, income int, party int, partyLean int, "
                 "PRIMARY KEY(person_id), FOREIGN KEY(person_id) "
                 "REFERENCES seal18_persons(person_id))")
        db.query(query)
        print('Create seal18_demographics table')

    @staticmethod
    def drop_table(db):
        query = 'DROP TABLE IF EXISTS seal18_demographics'
        db.query(query)
        print('Drop seal18_demographics table')

    @staticmethod
    def find_by_response_id(db, respid):
        query = ('SELECT person_id, sex, age, maritalStatus, education, '
                 'employment, race, income, party, partyLean '
                 'FROM seal18_demographics WHERE person_id = (%s)')
        return db.query(query, (respid,), 'fetchone')

    def save(self):
        keys = ', '.join(self.info.keys())
        vals = ', '.join(self.info.values())
        actual_keys = 'person_id, ' + keys
        actual_vals = str(self.respid) + ', ' + vals
        query = 'INSERT INTO seal18_demographics(' + actual_keys + ') VALUES (' + actual_vals + ')'
        self.db.query(query)
        print(query)

