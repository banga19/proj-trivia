import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = 'postgresql://{}/{}'.format("localhost:5432", 
            self.database_name)
        setup_db(self.app, self.database_path)

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
    # test for GET request to show all categories
    def test_retrieve_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assserEqual(data['categories'])

    # test to display when user request doesnt repsond to an existing category
    def test_404_sent_asking_for_non_existing_category(self):
        res = self.client().get('/categories/5683')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success', False])
        self.assertEqual(data['message'], 'resource not found')



    # test for GET endpoint responding to retrieving all paginated questions
    def test_retrieve_paginated_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_number_of_questions'])
        self.assertTrue(len(data['CureentQuestions']))
        self.assertTrue(len(data['categories']))

    #test 404 when user sends a request for a question beyond valid page
    def test_404_sent_asking_for_question_past_valid_page(self):
        res = self.client().get('/questions?page=1523')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')


    # test to DELETE specific using question_id
    def test_delete_specific_question(self):
        res = self.client().delete('questions/2')

        question_to_delete = Question.query.filter(Question.id == 2).one_or_none()
        self.assertEqual(question_to_delete, None)

    #test to CREATE new question 
    def test_create_new_question(self):
        res = self.client().post('questions', json={'question': 'Heres a new question in form of a string', 'answer': 'Here is an answer string', 'difficulty':1, 'category':3})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    # 404 ERROR HANDLER test past a valid page request
    def test_404_request_past_valid_page(self):
        res = self.client().get("/questions/1000", json=({'answer': 'Impossible'}))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], 'Resource Not Found')



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()