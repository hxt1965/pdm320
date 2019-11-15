import devices as dev
from controllers.opinions import OpinionController
from controllers.person import PersonController
from controllers.questions import QuestionsController
from controllers.social_media import SocialMediaController
from shared.database import Database


def load_person(file_name, database):
    person_controller = PersonController(file_name, database)
    person_controller.init_table_values()


def load_social_media(file_name, database):
    social_media_controller = SocialMediaController(file_name, database)
    social_media_controller.init_table_values()


def load_opinions(file_name, database):
    opinion_controller = OpinionController(file_name, database)
    opinion_controller.init_table_values()


def load_questions(file_name, database):
    question_controller = QuestionsController(file_name, database)
    question_controller.init_table_values()


def main():
    file_name = 'trends.csv'

    # Please use the same database instance for methods. Only create new database instance
    # if you must to. Using new database instance may produce error
    database = Database()

    # Comment those load methods out if you need to reload data
    load_person(file_name, database)
    load_social_media(file_name, database)
    load_questions(file_name, database)
    load_opinions(file_name, database)

    #a = database.query('SELECT * FROM seal18_questions', method='fetchall')
    #print(a)
    dev.main(file_name)

    return


if __name__ == '__main__':
    main()
