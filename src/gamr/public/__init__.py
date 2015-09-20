from flask import Flask
from flask.ext.cache import Cache
from gamr.scrapers import bfhl, wow, riot

app = Flask(__name__)

cache = Cache(app,config={'CACHE_TYPE': 'simple'})
cache.init_app(app)

@app.route('/hello')
@cache.cached(timeout=1440)
def hello():
    return str('Hello with cache!')
