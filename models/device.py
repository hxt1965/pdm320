class Device:
    def __init__(self, database, person_id, internet_service=None, has_cell_phone=None, phone_type=None,
                 has_tablet=None, has_computer=None, has_console=None):
        self.person_id = person_id
        self.internet_service = internet_service
        self.has_cell_phone = has_cell_phone
        self.phone_type = phone_type
        self.has_tablet = has_tablet
        self.has_computer = has_computer
        self.has_console = has_console
        self.database = database

    @staticmethod
    def create_table(database):
        query = """
                CREATE TABLE IF NOT EXISTS seal18_devices (
                    id SERIAL PRIMARY KEY,
                    person_id INTEGER REFERENCES seal18_persons (person_id) ON DELETE CASCADE,
                    internet_service text, 
                    has_cell_phone INTEGER,
                    phone_type INTEGER,
                    has_tablet INTEGER,
                    has_computer INTEGER,
                    has_console INTEGER
                )
                """
        database.query(query)
        print('Create seal18_devices table')

    @staticmethod
    def drop_table(database):
        query = 'DROP TABLE IF EXISTS seal18_devices'
        database.query(query)
        print('Drop seal18_devices table')

    def save(self):
        query = """
                INSERT INTO seal18_devices (
                    person_id, 
                    internet_service, 
                    has_cell_phone,
                    phone_type,
                    has_tablet,
                    has_computer,
                    has_console
                ) VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
        self.database.query(query, (
            self.person_id, self.internet_service, self.has_cell_phone, self.phone_type, self.has_tablet,
            self.has_computer,
            self.has_console))
        print(f'Saving a device for person with id {self.person_id} to the database')
