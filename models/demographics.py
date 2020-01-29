int_to_sex = {
    1: 'Male',
    2: 'Female'
}

int_to_marital = {
    1: 'Married',
    2: 'Living with a partner',
    3: 'Divorced',
    4: 'Separated',
    5: 'Widowed',
    6: 'Never been married',
    8: 'Don\'t know',
    9: 'Refused'
}

int_to_education = {
    1: 'Less than high school',
    2: 'High school incomplete',
    3: 'High school graduate',
    4: 'Some college, no degree',
    5: 'Two - year associate degree from a college or university',
    6: 'Four - year college or university degree / Bachelor’s degree',
    7: 'Some postgraduate or professional schooling, no postgraduate',
    8: 'Postgraduate or professional degree, including master’s, doctorate, medical or law degree',
    98: 'Don’t know',
    99: 'Refused'
}

int_to_employment = {
    1: 'Employed full-time',
    2: 'Employed part-time',
    3: 'Retired',
    4: 'Not employed for pay',
    5: 'Have own business / self-employed',
    6: 'Disabled',
    7: 'Student',
    8: 'Other',
    98: 'Don\'t know',
    99: 'Refused'
}

int_to_race = {
    1: 'White',
    2: 'Black or African-American',
    3: 'Asian or Asian-American',
    4: 'Some other race',
    5: 'Native American / American Indian / Alaska Native',
    6: 'Pacific Islander / Native Hawaiian',
    7: 'Hispanic / Latino',
    8: 'Don\'t know',
    9: 'Refused'
}

int_to_income = {
    1: 'Less than $10,000',
    2: '10 to under $20,000',
    3: '20 to under $30,000',
    4: '30 to under $40,000',
    5: '40 to under $50,000',
    6: '50 to under $75,000',
    7: '75 to under $100,000',
    8: '100 to under $150,000',
    9: '$150,000 or more',
    98: 'Don\'t know',
    99: 'Refused'
}

int_to_party = {
    1: 'Republican',
    2: 'Democrat',
    3: 'Independent',
    4: 'No preference',
    5: 'Other party',
    8: 'Don\'t know',
    9: 'Refused'
}

int_to_party_lean = {
    1: 'Republican',
    2: 'Democrat',
    8: 'Don\'t know',
    9: 'Refused'
}


class Demographics:
    def __init__(self, database, response_id, info):
        self.person_id = int(response_id)
        self.db = database
        self.info = info

    @staticmethod
    def create_table(db):
        query = """
                CREATE TABLE IF NOT EXISTS seal18_demographics(
                    id serial primary key,
                    person_id int NOT NULL REFERENCES seal18_persons(person_id), 
                    sex int, 
                    age int,
                    maritalStatus int, 
                    education int, 
                    employment int,
                    race int, 
                    income int, 
                    party int, 
                    partyLean int
                )
                 """
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
