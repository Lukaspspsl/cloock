from flask import Flask, render_template
from flask_smorest import Api, Blueprint
from datetime import datetime


app = Flask(__name__)
app.config['API_TITLE'] = 'Clock API'
app.config['API_VERSION'] = 'v1'
app.config["OPENAPI_VERSION"] = "3.0.2"
api = Api(app)

bp = Blueprint('time', __name__, url_prefix='/api/time')


@bp.route('/')
def get_time():
    return {'time': datetime.now().strftime('%H:%M:%S')}


@app.route('/')
def index():
    return render_template('index.html')


api.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True)
