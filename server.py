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


@app.route('/')
def index():
    """homepage"""

    return render_template("FirstPage_Search.htm")


@app.route('/search_results', methods=['POST'])
def search_results():
    """Results of driver search"""

    return render_template("Results.htm")


@app.route('/survey')
def survey():
    """Survey"""

    return render_template("Survey.htm")


@app.route('/save', methods=['POST'])
def save_survey_results():
    """Save survey results from form"""

    user_id = request.form.get("user_id")
    driver_id = request.form.get("driver_id")
    rating = request.form.get("rating")
    punctuality = request.form.get("punctuality")
    drop_off = request.form.get("drop_off")
    special_instructions = request.form.get("special_instructions")
    feel_safe = request.form.get("feel_safe")
    driving_reckless = request.form.get("driving_reckless")
    harassment = request.form.get("harassment")
    comment = request.form.get("comment")

    new_log = Ratings(user_id=user_id, driver_id=driver_id, rating=rating, punctuality=punctuality,
                      drop_off=drop_off, special_instructions=special_instructions,
                      feel_safe=feel_safe, driving_reckless=driving_reckless,
                      harassment=harassment, comment=comment)

    db.session.add(new_log)
    db.session.commit()



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
