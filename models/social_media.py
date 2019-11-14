class SocialMedia:
    freq_to_text = {
        '1': 'Several times a day',
        '2': 'About once a day',
        '3': 'A few times a week',
        '4': 'Every few weeks',
        '5': 'Less often',
        '8': 'Don\'t know',
        '9': 'Refused',
        '10': 'Empty'
    }

    def __init__(self, person_id, name, freq, database):
        self.person_id = person_id
        self.name = name
        self.freq = freq
        self.database = database

    @staticmethod
    def create_table(database):
        query = 'CREATE TABLE IF NOT EXISTS seal18_social_medias (id SERIAL PRIMARY KEY, person_id INTEGER REFERENCES ' \
                'seal18_persons (id) ON DELETE CASCADE, name VARCHAR(20) NOT NULL, freq INTEGER DEFAULT 0) '
        database.query(query)
        print('Create seal18_social_medias table')

    @staticmethod
    def drop_table(database):
        query = 'DROP TABLE IF EXISTS seal18_social_medias'
        database.query(query)
        print('Drop seal18_social_medias table')

    def save(self):
        query = 'INSERT INTO seal18_social_medias (person_id, name, freq) VALUES (%s, %s, %s)'
        self.database.query(query, (self.person_id, self.name, self.freq))
        print(
            f'Saving a social media with name is {self.name} person_id is {self.person_id} and frequency is {self.freq} to the database')
