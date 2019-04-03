from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import  g, send_file, request, redirect,jsonify
from functools import wraps
#import jwt
import datetime
import config





app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class users(db.Model):
   email = db.Column(db.String(100), primary_key = True)
   password = db.Column(db.String(50))
   
   def __init__(self, email,password):
      self.email= email
      self.password = password

   def token(self):
        payload = {
            'email': self.email
        }
        # token = jwt.encode(payload, config['TOKEN_SECRET'])
        token = "SOMETHING_RANDOM_TO_SAY"
        return token

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['email'] or not request.form['password']:
         flash('Please enter all the fields', 'error')
      else:
         user = users(request.form['email'], request.form['password'])
         
         db.session.add(user)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('show_all'))
   return render_template('new.html')



def parse_token(req):
    token = req.headers.get('Authorization').split()[1]
    return jwt.decode(token, config.TOKEN_SECRET)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not request.headers.get('Authorization'):
            response = jsonify(message='Missing authorization header')
            response.status_code = 401
            return response

        try:
            payload = parse_token(request)
        except Exception:
            response = jsonify(message='Token is invalid')
            response.status_code = 401
            return response

        g.user_id = payload['sub']

        return f(*args, **kwargs)

    return decorated_function


def jsonify_resp(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        
        resp, status = f(*args, **kwargs)
        return jsonify(resp), status

    return decorated_function


@app.route('/auth/signup', methods=['POST'])
def signup():
    data = request.json

    email = data["email"]
    password = data["password"]

    user = users(email=email, password=password)
    db.session.add(user)
    db.session.commit()

    return jsonify(token=user.token())


@app.route('/auth/login', methods=['POST'])
def login():
    data = request.json

    email = data.get("email")
    print (email)
    password = str(data.get("password"))
    print (password)
    print (type(password))

    user = db.session.query(users).filter_by(email=email).first()
    if not user:
        return jsonify(error="No such user"), 404

    password_ascii = password.encode('ascii','ignore')
    password_uni = password_ascii.decode("utf-8")
    print(password_uni)
    print(type(password_uni))
    if user.password == password_uni:
        return jsonify(token=user.token()), 200
    else:
        return jsonify(error="Wrong email or password"), 400


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not request.headers.get('Authorization'):
            response = jsonify(message='Missing authorization header')
            response.status_code = 401
            return response

    return decorated_function



if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)