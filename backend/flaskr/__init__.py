import os
from unicodedata import category
from select import select
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random


from models import setup_db, Question, Category

# global GET categories func
def func_get_categories():
    categories = Category.query.order_by(Category.id).all()
    category_obj = {}
    for category in categories:
        category_obj[Category.id] = category.type()
    return category_obj
    
# pagination
QUESTIONS_PER_PAGE = 10

# create pagination effect for the app
def paginated_guestions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    books = [question.format() for question in selection]
    current_questions = books[start:end]

    return current_questions


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
        categories = func_get_categories()

        return jsonify({
            "success": True,
            "categories": categories,
        })


    #GET questions endpoint
    @app.route('/questions', methods=['GET'])
    def retrieve_paginated_questions():
        selection = Question.query.order_by(Question.id).all()
        current_questions = paginated_guestions(request, selection)
        categories = func_get_categories()

        if current_questions == 0:
            abort(404)
        else:
            return jsonify({
                "succes": True,
                "categories": categories,
                "total_number_of_questions": len(Question.query.all()),
                "questions": current_questions,
                "currentCategory": categories
            })



    # DELETE specific question endpoint
    @app.route('/questions/<int:question_id>', methods=["DELETE"])
    def delete_specific_question(question_id):
        question = Question.query.get(question_id)

        if question is not None:
            question.delete()

            return jsonify({
                "success": True,
                "deleted_question": question,
            })
        else:
            abort(404)
            


    # POST create & add new question based on a search term 
    @app.route('/questions', methods=['POST'])
    def create_new_question():
        body = request.get_json()
        new_question = body.get('question', None)
        new_answer = body.get('answer', None)
        new_difficulty = body.get('difficulty', None)
        new_category = body.get('category', None)
        search = body.get('searchTerm', None)

        if search:
            selection = Question.query.order_by(Question.id).filter(Question.question.ilike('%{}%'.format(search)))
            current_question = paginated_guestions(request, selection)
            return jsonify({
                "success": True,
                "questions": current_question,
                "total_number_of_questions": len(Question.query.all()), ##find out if the 'key' is corresponding with frontend value # ie --> var = totalQuestions#
                "CurrentCategory": 'Entertainment'
            })
        
        else:
            add_question = Question(
                question = new_question,
                answer = new_answer,
                difficulty = new_difficulty,
                category = new_category,
            )

            add_question.insert()

            return jsonify({
                'success': True,
            })
    
    # GET endpoint to retrieve questions from DB in a specific category
    @app.route('/categories/<int:category_id>/questions', methods=['POST'])
    def retrieve_question_by_category(category_id):
        selection = Question.query.order_by(Question.id).filter(Question.category == category_id)
        current_questions = paginated_guestions(request, selection)

        if selection:
            return jsonify({
                'questions': current_questions,
                'totalQuestions': len(Question.query.all()),
                'currentCategory': current_questions
            })
        else:
            abort(404)
    

    # POST endpoint to get questions to play the quiz
    @app.route('/quizes', methods=['POST'])
    def display_random_quizes():
        body = request.get_json()
        previous_questions = body.get('previous_questions', None)
        quiz_category = body.get('quiz_category', None)

        questions = Question.query.oder_by(Question.id).filter(Question.category == quiz_category['id'])
        user_selected_question = []

        for question in questions:
            if question.id not in previous_questions:
                user_selected_question.append(question)
            
            else:
                return print("Could Not process request, Try Again")


        random_index = random.randrange(len(user_selected_question))
        random_question = user_selected_question[random_index]

        return jsonify({
            "success": True,
            "Random Question": random_question
            
        })


# ERROR HANDLER ENDPOINTS
# 404 ERROR endpoint
    @app.errorhandler(404)
    def resource_not_found(error):
        return jsonify({
            "success":False,
            "error": 404,
            "message": "Resource Not Found"
        }), 404

# 405 ERROR handler
    @app.errorhandler(405)
    def action_not_allowed(error):
        return jsonify({
            "succes": False,
            "error": 405,
            "message": "Method Not Allowed"
        }), 405

# 422 Error Handler
    @app.errorhandler(422)
    def unable_to_process(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unable to process request. Try Again",
        }), 422

    return app

