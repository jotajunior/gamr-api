from flask import Flask, request
from flask.ext.cache import Cache
from gamr.controller.user import User
from gamr.controller.survey import Survey

app = Flask(__name__)

cache = Cache(app,config={'CACHE_TYPE': 'simple'})
cache.init_app(app)

@app.route('/user', methods=['POST'])
def user_post():
    result = User().get(request.form['WOW_id'],
                      request.form['WOW_realm'],
                      request.form['WOW_region'],
                      request.form['BFHD_id'],
                      'pc',
                      request.form['BF4_id'],
                      'pc',
                      request.form['LOL_id'],
                      request.form['LOL_region'],
                      request.form['birth_year'],
                      request.form['birth_month'],
                      request.form['country'],
                      request.form['english_lvl'],
                      request.form['gender'],
                      )
    return result

if __name__ == '__main__':
    app.run(debug=True)
