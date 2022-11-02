import os
from unicodedata import category
from urllib import response
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category



QUESTIONS_PER_PAGE = 10

# creating the pagination effect for the app
def paginated_guestions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    books = [question.format() for question in selection]
    current_questions = books[start:end] 

# global GET categories func
def get_categories_func():
    categories = Category.query.order_by(Category.id).all()
    category_obj = {}
    for category in categories:
        category_obj[category.id] = category.type
    return category_obj
    
# Start of trivia app
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    
    #CORS initialization to ensure secure data acces & transmission accross multiple domains
    CORS(app, resources={r"*": {"origins":"*"}})

    # Allowing CORS TO work on trivia app
    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization,true")
        response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")

        return response


# GET Categories endpoint   
    @app.route('/categories', methods=['GET'])
    def retrieve_categories():
        categories = get_categories_func()
        return jsonify({
            "success": True,
            "categories": categories,
        })


#GET questions endpoint
    @app.route('/questions', methods=['GET'])
    def retrieve_questions():
        selection = Question.query.order_by(Question.id).all()
        current_questions = paginated_guestions(request, selection)
        categories = get_categories_func()

        if current_questions == 0:
            abort(404)
        else:
            return jsonify({
                "succes": True,
                "categories": categories,
                "total_number_of_questions": len(Question.query.all()),
                "questions": current_questions,
                "currentCategory": 'Science'
            })


    """

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """
# DELETE specific question endpoint
    @app.route('/questions/<int:question_id>', methods=["DELETE"])
    def delete_specific_question(question_id):
        question = Question.query.get(question_id)

        if question is not None:
            question.delete()

            return jsonify({
                "success": True
            })
        else:
            abort(404)
            
    """
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """
# POST create new question
    @app.route('/questions', methods=['POST'])
    def new_question():
        return jsonify({
            "success": True,
        })
    """
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """

    """
    @TODO:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """

    """
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """

    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """

    return app

