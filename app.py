from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.academia import academias_route
from routes.sobre import sobre_route
from routes.home import home_route


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///suaacademia.db'
db = SQLAlchemy(app)
app.register_blueprint(home_route)
app.register_blueprint(academias_route)
app.register_blueprint(sobre_route)

if __name__ == '__main__':
    app.run(debug=True)