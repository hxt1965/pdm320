class Demographics:
    def __init__(self, database, response_id, info):
        self.person_id = int(response_id)
        self.db = database
        self.info = info

    @staticmethod
    def create_table(db):
        query = ("CREATE TABLE IF NOT EXISTS seal18_demographics("
                 "id serial primary key, "
                 "person_id int NOT NULL REFERENCES seal18_persons(person_id), sex int, age int, "
                 "maritalStatus int, education int, employment int, "
                 "race int, income int, party int, partyLean int)")
        db.query(query)
        print('Create seal18_demographics table')

    @staticmethod
    def drop_table(db):
        query = 'DROP TABLE IF EXISTS seal18_demographics'
        db.query(query)
        print('Drop seal18_demographics table')

    @staticmethod
    def find_by_person_id(db, respid):
        query = ('SELECT person_id, sex, age, maritalStatus, education, '
                 'employment, race, income, party, partyLean '
                 'FROM seal18_demographics WHERE person_id = (%s)')
        return db.query(query, (respid,), 'fetchone')

    def save(self):
        sex = int(self.info['sex']) if self.info['sex'] is not None else None
        age = int(self.info['age']) if self.info['age'] is not None else None
        maritalStatus = int(self.info['maritalStatus']) if self.info['maritalStatus'] is not None else None
        education = int(self.info['education']) if self.info['education'] is not None else None
        employment = int(self.info['employment']) if self.info['employment'] is not None else None
        race = int(self.info['race']) if self.info['race'] is not None else None
        income = int(self.info['income']) if self.info['income'] is not None else None
        party = int(self.info['party']) if self.info['party'] is not None else None
        partyLean = int(self.info['partyLean']) if self.info['partyLean'] is not None else None
        query = 'INSERT INTO seal18_demographics (person_id, sex, age, maritalStatus, education, employment, race, ' \
                'income, party, partyLean) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) '
        self.db.query(query,
                      (self.person_id, sex, age, maritalStatus, education, employment, race, income, party, partyLean))
        print(f'Saving a demographics for person with id {self.person_id} and info {self.info} to the database')
