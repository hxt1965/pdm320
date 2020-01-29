import pandas

from models.social_media import SocialMedia


class SocialMediaController:
    def __init__(self, file_name, database):
        self.df = pandas.read_csv(file_name)
        self.rows = self.df.shape[0]
        self.database = database

    def init_table_values(self):
        suffix = ['a', 'b', 'c', 'd', 'e']
        columns_to_name = {
            'web1a': 'Twitter',
            'web1b': 'Instagram',
            'web1c': 'Facebook',
            'web1d': 'Snapchat',
            'web1e': 'Youtube',
        }
        columns_to_freq_text = {
            1: 'Several times a day',
            2: 'About once a day',
            3: 'A few times a week',
            4: 'Every few weeks',
            5: 'Less often',
            8: 'Don\'t know',
            9: 'Refused'
        }

        SocialMedia.drop_table(self.database)
        SocialMedia.create_table(self.database)

        for i in range(self.rows):
            response_id = int(self.df['respid'][i])
            for char in suffix:
                freq_key = f'sns2{char}'
                key = f'web1{char}'
                name = columns_to_name[key]
                if (not pandas.isna(self.df[key][i])):
                    use = int(self.df[key][i])
                    freq = 0
                    freq_text = None
                    if (use == 1 or use == 2):
                        is_using = False
                        if (use == 1):
                            is_using = True
                            freq = int(self.df[freq_key][i])
                            freq_text = columns_to_freq_text[freq]

                        social_media = SocialMedia(response_id, name, is_using, freq, freq_text, self.database)
                        social_media.save()
