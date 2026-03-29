# import classes
from flask import Flask
from views import views

# creates flask application and conects to routes in views.py
app = Flask(__name__)
app.register_blueprint(views)

# runs dev server when executed, assigning it a port to run on
if __name__ == '__main__':
    app.run(debug=True, port=8000)