from flask import Flask, render_template
from flask_smorest import Api, Blueprint
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from datetime import datetime
import logging


app = Flask(__name__)
app.config['API_TITLE'] = 'Clock API'
app.config['API_VERSION'] = 'v1'
app.config["OPENAPI_VERSION"] = "3.0.2"
api = Api(app)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["20 per minute"],
    storage_uri="memory://",
)

logging.basicConfig(level=logging.INFO)

bp = Blueprint('time', __name__, url_prefix='/api/time')


@limiter.limit("5 per minute")
@bp.route('/')
def get_time():
    logging.info("get_time function executed")
    return {'time': datetime.now().strftime('%H:%M:%S')}


@app.route('/')
def render_index():
    logging.info("Rendering index.html")
    return render_template('index.html')


api.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=False)


