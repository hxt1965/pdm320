import pandas

from models.person import Person
from models.social_media import SocialMedia


class SocialMediaController:
    def __init__(self, file_name, database):
        self.df = pandas.read_csv(file_name)
        self.rows = self.df.shape[0]
        self.database = database

    def init_table_values(self):
        columns_to_name = {
            'web1a': 'Twitter',
            'web1b': 'Instagram',
            'web1c': 'Facebook',
            'web1d': 'Snapchat',
            'web1e': 'Youtube',
        }
        SocialMedia.drop_table(self.database)
        SocialMedia.create_table(self.database)

        for i in range(self.rows):
            response_id = int(self.df['respid'][i])
            person = Person.find_by_response_id(response_id, self.database)
            if (person is None):
                raise Exception('Cannot find person for response_id. You may need to load your persons data again')

            person_id = int(person['id'])

            for key in columns_to_name.keys():
                name = columns_to_name[key]
                if (pandas.isna(self.df[key][i])):
                    freq = 10
                else:
                    freq = int(self.df[key][i])

                social_media = SocialMedia(person_id, name, freq, self.database)
                social_media.save()
