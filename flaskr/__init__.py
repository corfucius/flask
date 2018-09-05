import os

from flask import Flask

def create_app(test_config=None):
    #create and configure app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    ) 

    if test_config is None:
        #load the instance config, if it exists
        app.config.from_pyfile('config.py', silent=True)
    else:
        #load test config 
        app.config.from_mapping(test_config)
    
    #ensure insance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    # a simple page to say hello
    @app.route('/hello')
    def hello():
        return 'hello again, ugh'

    from . import db
    db.init_app(app)
    
    return app