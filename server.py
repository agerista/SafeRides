from jinja2 import StrictUndefined
from flask import Flask, jsonify, render_template, redirect, request, flash, session
# from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, User, Driver, Ratings

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "saferidesrule"

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined

@app.route('/', methods=['GET'])
def index():
    """homepage"""

    return render_template("FirstPage_Search.htm")


@app.route('/', methods=['POST'])
def index():
    """homepage"""

    driver = Driver.query.filter_by(zipcode=zipcode).all()
    print driver

    return render_template("FirstPage_Search.htm", driver=driver)


@app.route('/search_results')
def search_results():
    """Results of driver search"""

    

    return render_template("search_results.htm")



################################################################################
if __name__ == "__main__":

    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = False
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)
    app.run(port=5000, host='0.0.0.0')
