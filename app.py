from flask import Flask
from routes.academia import academias_route
from routes.sobre import sobre_route
from routes.home import home_route


app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(academias_route)
app.register_blueprint(sobre_route)



app.run(debug=True)