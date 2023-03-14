from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask import send_file

from config import CONFIG
# import from parent directory
#import sys
#sys.path.append('../')
from answers import df, answer_question


app = Flask(__name__)
api = Api(app)

answers_post_args = reqparse.RequestParser()
answers_post_args.add_argument("question", type=str, help="Question to be answered")


class Answers(Resource):
  def post(self):
    global df
    args= answers_post_args.parse_args()
    answer= answer_question(df, question=args.question, log_answer=CONFIG['log_answers'], answers_log_file=CONFIG['answers_log_file'])
    return {'question': args.question, 'answer':answer}
  
api.add_resource(Answers, '/api/answers')


@app.route('/')
def home():
  try:
    #return send_file('./index.html', attachment_filename='index.html')
    return send_file('./index.html')
  except Exception as e:
    return str(e)

if __name__ == "__main__":
  app.run(debug=True)