# Backend - Trivia API

## Setting up the Backend

### Install Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

### Set up the Database

With Postgres running, create a `trivia` database:

```bash
createdb trivia
```

Populate the database using the `trivia.psql` file provided. From the `backend` folder in terminal run:

```bash
psql trivia < trivia.psql
```

### Run the Server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## To Do Tasks

These are the files you'd want to edit in the backend:

1. `backend/flaskr/__init__.py`
2. `backend/test_flaskr.py`

One note before you delve into your tasks: for each endpoint, you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior.

1. Use Flask-CORS to enable cross-domain requests and set response headers.
2. Create an endpoint to handle `GET` requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories.
3. Create an endpoint to handle `GET` requests for all available categories.
4. Create an endpoint to `DELETE` a question using a question `ID`.
5. Create an endpoint to `POST` a new question, which will require the question and answer text, category, and difficulty score.
6. Create a `POST` endpoint to get questions based on category.
7. Create a `POST` endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question.
8. Create a `POST` endpoint to get questions to play the quiz. This endpoint should take a category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions.
9. Create error handlers for all expected errors including 400, 404, 422, and 500.

## Documenting your Endpoints

You will need to provide detailed documentation of your API endpoints including the URL, request parameters, and the response body. Use the example below as a reference.


### Running the server in Dev mode
The frontend app was built using create-react-app. In order to run the app in development mode use npm start. You can change the script in the package.json file.

Open http://localhost:3000 to view it in the browser. The page will reload if you make edits.

`npm start` 



# API reference
## start of Endpoint Documentation for sample requests

`GET /api/questions`
- `sample: curl http://127.0.0.1:5000/questions`

- This endpoint will handle GET requests for questions, including pagination (every 10 questions), stored in the database 
- Request Arguments: None
- returns: returns a list of questions, number of total questions, current category, categories.


``` json
 {
      "categories": {
          "1": "Science", 
          "2": "Art", 
          "3": "Geography", 
          "4": "History", 
          "5": "Entertainment", 
          "6": "Sports"
      }, 
      "questions": [
          {
              "answer": "Colorado, New Mexico, Arizona, Utah", 
              "category": 3, 
              "difficulty": 3, 
              "id": 164, 
              "question": "Which four states make up the 4 Corners region of the US?"
          }, 
          {
              "answer": "Muhammad Ali", 
              "category": 4, 
              "difficulty": 1, 
              "id": 9, 
              "question": "What boxer's original name is Cassius Clay?"
          }, 
          {
              "answer": "Apollo 13", 
              "category": 5, 
              "difficulty": 4, 
              "id": 2, 
              "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
          }, 
          {
              "answer": "Tom Cruise", 
              "category": 5, 
              "difficulty": 4, 
              "id": 4, 
              "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
          }, 
          {
              "answer": "Edward Scissorhands", 
              "category": 5, 
              "difficulty": 3, 
              "id": 6, 
              "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
          }, 
          {
              "answer": "Brazil", 
              "category": 6, 
              "difficulty": 3, 
              "id": 10, 
              "question": "Which is the only team to play in every soccer World Cup tournament?"
          }, 
          {
              "answer": "Uruguay", 
              "category": 6, 
              "difficulty": 4, 
              "id": 11, 
              "question": "Which country won the first ever soccer World Cup in 1930?"
          }, 
          {
              "answer": "George Washington Carver", 
              "category": 4, 
              "difficulty": 2, 
              "id": 12, 
              "question": "Who invented Peanut Butter?"
          }, 
          {
              "answer": "Lake Victoria", 
              "category": 3, 
              "difficulty": 2, 
              "id": 13, 
              "question": "What is the largest lake in Africa?"
          }, 
          {
              "answer": "The Palace of Versailles", 
              "category": 3, 
              "difficulty": 3, 
              "id": 14, 
              "question": "In which royal palace would you find the Hall of Mirrors?"
          }
      ], 
      "success": true, 
      "total_questions": 19
  }
```

`GET /api/categories`
  - `sample: curl -X GET http://127.0.0.1:5000/categories`
- fetches for all available categories in the DATABASE
- request parameters: None
- return: list of categories in json format

``` json
  "categories": 
          {
            "1": "Science",
            "2": "Art",
            "3": "Geography",
            "4": "History",
            "5": "Entertainment",
            "6": "Sports"
          },
          "success": true,
```

`DELETE /question/${id}`
  `sample: curl -X DELETE http://127.0.0.1:5000/questions/5`
- DELETES question selected by user according to the Id
- request parameters: question_id
- return: A statment saying the deleted question using the 'ID' as the key and the 'specific question' as the value

``` json
{
  "delted_quesition": 5,
  "success": true 
}

```


` POST /api/questions`

- endpoint adds new question or returns search results

1. situation where **no** search term is addes to the request:
    - It will create a new question using JSON request parameters
    - Returns a JSON object with newly added question, in paginated form
    - sample: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{ "question": "Which US state contains an area known as the Upper Penninsula?", "answer": "Michigan", "difficulty": 3, "category": "3" }'` 

``` json
  {
      "created": 173, 
      "question_created": "Which US state contains an area known as the Upper Penninsula?", 
      "questions": [
          {
              "answer": "Apollo 13", 
              "category": 5, 
              "difficulty": 4, 
              "id": 2, 
              "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
          }, 
          {
              "answer": "Tom Cruise", 
              "category": 5, 
              "difficulty": 4, 
              "id": 4, 
              "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
          }, 
          {
              "answer": "Muhammad Ali", 
              "category": 4, 
              "difficulty": 1, 
              "id": 9, 
              "question": "What boxer's original name is Cassius Clay?"
          }, 
          {
              "answer": "Brazil", 
              "category": 6, 
              "difficulty": 3, 
              "id": 10, 
              "question": "Which is the only team to play in every soccer World Cup tournament?"
          }, 
          {
              "answer": "Uruguay", 
              "category": 6, 
              "difficulty": 4, 
              "id": 11, 
              "question": "Which country won the first ever soccer World Cup in 1930?"
          }, 
          {
              "answer": "George Washington Carver", 
              "category": 4, 
              "difficulty": 2, 
              "id": 12, 
              "question": "Who invented Peanut Butter?"
          }, 
          {
              "answer": "Lake Victoria", 
              "category": 3, 
              "difficulty": 2, 
              "id": 13, 
              "question": "What is the largest lake in Africa?"
          }, 
          {
              "answer": "The Palace of Versailles", 
              "category": 3, 
              "difficulty": 3, 
              "id": 14, 
              "question": "In which royal palace would you find the Hall of Mirrors?"
          }, 
          {
              "answer": "Agra", 
              "category": 3, 
              "difficulty": 2, 
              "id": 15, 
              "question": "The Taj Mahal is located in which Indian city?"
          }, 
          {
              "answer": "Escher", 
              "category": 2, 
              "difficulty": 1, 
              "id": 16, 
              "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
          }
      ], 
      "success": true, 
      "total_questions": 20
  }
```


2. situation where search term **is** included:
    - function below decorator will search for questions using search term in JSON request parameters.
    - It will then return a JSON object with matching questions in paginated format
    - sample: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"searchTerm": "which"}'`

``` json
  {
      "questions": [
          {
              "answer": "Brazil", 
              "category": 6, 
              "difficulty": 3, 
              "id": 10, 
              "question": "Which is the only team to play in every soccer World Cup tournament?"
          }, 
          {
              "answer": "Uruguay", 
              "category": 6, 
              "difficulty": 4, 
              "id": 11, 
              "question": "Which country won the first ever soccer World Cup in 1930?"
          }, 
          {
              "answer": "The Palace of Versailles", 
              "category": 3, 
              "difficulty": 3, 
              "id": 14, 
              "question": "In which royal palace would you find the Hall of Mirrors?"
          }, 
          {
              "answer": "Agra", 
              "category": 3, 
              "difficulty": 2, 
              "id": 15, 
              "question": "The Taj Mahal is located in which Indian city?"
          }, 
          {
              "answer": "Escher", 
              "category": 2, 
              "difficulty": 1, 
              "id": 16, 
              "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
          }, 
          {
              "answer": "Jackson Pollock", 
              "category": 2, 
              "difficulty": 2, 
              "id": 19, 
              "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
          }, 
          {
              "answer": "Scarab", 
              "category": 4, 
              "difficulty": 4, 
              "id": 23, 
              "question": "Which dung beetle was worshipped by the ancient Egyptians?"
          }, 
          {
              "answer": "Michigan", 
              "category": 3, 
              "difficulty": 3, 
              "id": 173, 
              "question": "Which US state contains an area known as the Upper Penninsula?"
          }
      ], 
      "success": true, 
      "total_questions": 18
  }
```


`GET /api/categories/${category_id}/questions`

- fetches all questions in a specific category using the id
- Returns a JSON object of the questions in a paginated format
- sample: `curl http://127.0.0.1:5000/categories/5/questions`

``` json
  {
      "current_category": "Science", 
      "questions": [
          {
              "answer": "The Liver", 
              "category": 1, 
              "difficulty": 4, 
              "id": 20, 
              "question": "What is the heaviest organ in the human body?"
          }, 
          {
              "answer": "Alexander Fleming", 
              "category": 1, 
              "difficulty": 3, 
              "id": 21, 
              "question": "Who discovered penicillin?"
          }, 
          {
              "answer": "Blood", 
              "category": 1, 
              "difficulty": 4, 
              "id": 22, 
              "question": "Hematology is a branch of medicine involving the study of what?"
          }
      ], 
      "success": true, 
      "total_questions": 18
  }
```

`POST /quizes`
- allows users to play the actual quiz
- fetches questions to play the quiz 
- request parameteres: category, previous_questions
- It will return a JSON object with random question not among previous questions.
- sample URL: `curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions": [20, 21], "quiz_category": {"type": "Science", "id": "1"}}'`

```json
  {
      "question": {
          "answer": "Blood", 
          "category": 1, 
          "difficulty": 4, 
          "id": 22, 
          "question": "Hematology is a branch of medicine involving the study of what?"
      }, 
      "success": true
  }
```


## Error Handling 

When the errors occur, they are returned as a JSON format like example below:

```json
{
    "success": False,
    "error": 404,
    "message": "resource not found"
}
```

The Trivia API will return three types of errors as follows:
- 400: repsonsible dealing with bad requests
- 404: reponsible for dealing with resources not found 
- 422: deals with a unprocessable request


## Testing

Write at least one test for the success and at least one error behavior of each endpoint using the unittest library.

To deploy the tests, run

```bash
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
