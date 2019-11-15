import pandas
import math

from models.demographics import Demographics


class DemographicsController:

    def __init__(self, file_name, database):
        self.df = pandas.read_csv(file_name)
        self.rows = self.df.shape[0]
        self.database = database

    def init_table_values(self):
        Demographics.drop_table(self.database)
        Demographics.create_table(self.database)

        for i in range(self.rows):
            person_id = int(self.df['respid'][i])
            sex = int(self.df['sex'][i])
            age = int(self.df['age'][i])
            if age > 97:
                age = None
            maritalStatus = int(self.df['marital'][i])
            if maritalStatus > 6:
                maritalStatus = None
            education = int(self.df['educ2'][i])
            if education > 8:
                education = None
            employment = int(self.df['emplnw'][i])
            if employment > 8:
                employment = None
            race = self.get_person_race(i)
            income = int(self.df['inc'][i])
            if income > 9:
                income = None
            party = int(self.df['party'][i])
            if party > 5:
                party = None
            partyLean = 0
            if not math.isnan(self.df['partyln'][i]):
                partyLean = int(self.df['partyln'][i])

            data = {'sex': sex, 'age': age, 'maritalStatus': maritalStatus,
                    'education': education, 'employment': employment,
                    'race': race, 'income': income, 'party': party, 'partyLean': partyLean}
            demographic_p = Demographics(self.database, person_id, data)
            demographic_p.save()

    """
    Gets a bit-encoded integer represents of all the races
    this person is
    """
    def get_person_race(self, i):
        race1 = int(self.df['racem1'][i])
        race2 = self.df['racem2'][i]
        race3 = self.df['racem3'][i]
        race4 = self.df['racem4'][i]
        if race1 > 7:  # refused to answer
            return None
        overall_race = (1 << race1)
        if not math.isnan(race2):
            overall_race |= (1 << int(race2))
        if not math.isnan(race3):
            overall_race |= (1 << int(race3))
        if not math.isnan(race4):
            overall_race |= (1 << int(race4))
        return overall_race
