import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from backend.flaskr.models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_user = "student"
        self.database_password = "student"
        self.database_path = 'postgresql+psycopg2://{}:{}@{}/{}'.format(
            self.database_user, self.database_password, 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # sample question for use in testing the api
        self.new_question = {
            'question': 'Which four states make up the 4 Corners region of the US?',
            'answer': 'Colorado, New Mexico, Arizona, Utah',
            'difficulty': 3,
            'category': '3'
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    # test below to GET reponse and add data. 
    # it will also test for pagination success
    def test_get_questions_paginated(self):

        response = self.client().get('/questions') 
        data = json.loads(response.data)

        # check for status code and message
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['succes'], True)

        # check total questions and returns and the questions return data
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()