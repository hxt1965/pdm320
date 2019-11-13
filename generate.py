import demographics as dem
import devices as dev
import opinions as op

from controllers.person import PersonController
from controllers.social_media import SocialMediaController
from shared.database import Database


def main():
    database = Database()
    file_name = 'trends.csv'

    op.main('trends.csv')
    dem.main('trends.csv')
    dev.main('trends.csv')

    # person_controller = PersonController(file_name, database)
    # person_controller.init_table_values()

    social_media_controller = SocialMediaController(file_name, database)
    social_media_controller.init_table_values()

    return


if __name__ == '__main__':
    main()
