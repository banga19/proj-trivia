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
        self.database_path = 'postgresql://{}@{}:{}/{}'.format("student", "student","localhost:5432", 
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
    
    # test to delete specific question Failure scenario
    def test_422_deleting_non_existing_question(self):
        res = self.client().delete('/question/12')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success', False])
        self.assertEqual(data['message'], 'Request Unprocessable')
    

    #test to ADD new question 
    def test_add_new_question(self):
        res = self.client().post('questions', json={'question': 'Heres a new question in form of a string', 'answer': 'Here is an answer string', 'difficulty':1, 'category':3})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    # test to show failure when adding new question
    def test_for_422_error_adding_new_question(self):
        new_question = {
            'question': 'is a fork a spoon?',
            'answer': 'user answer',
            'category': 5,
        }
        res = self.client().post('/questions', json=new_question)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Request Unproccesable')

    # test for user request success scenario when searching for a question
    def test_search_questions_success_screnario(self):
        new_user_search_term = {'searchTerm': 'sq343841'}
        res = self.client().post('/questions/search', json=new_user_search_term)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(data['questions'])
        self.assertIsNotNone(data['total_questions_available'])

    # test for user request success scenario when searching for a question
    def test_404_search_question_failure_scenario(self):
        new_user_search_term = {
            'searchTerm': '899*^$5--',
        }
        res = self.client().post('/question/search', json=new_user_search_term)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['sucess'], False)
        self.assertEqual(data['message'], "The resource you are looking for cannot be found")

    # test success scenario for getting questions by category
    def test_retrieve_questions_by_category(self):
        res = self.client().get('/categories/3/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions_available'])
        self.assertTrue(data['current-category'])

    # test failure scenario for getting questions by category
    def test_404_to_retrieve_questions_by_category(self):
        res = self.client().get('/categories/l/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "The resource you are looking for could not be found")

    # test success scenario for when user plays actual quiz
    def test_display_random_quizes_to_play(self):
        new_quiz_session_play = {'previous_questions': [],
                            'quiz_category': {'type': 'History', 'id': 3}}

        res = self.client().post('/quizzes', json=new_quiz_session_play)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    #test failure scenario for for when user plays actual quiz
    def test_404_play_quiz_in_random(self):
        new_quiz_session_play = {'previous_questions': []}
        res = self.client().post('/quizzes', json=new_quiz_session_play)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Request Unprocessable")

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