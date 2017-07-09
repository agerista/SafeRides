"""Models and database functions for Safe Rides Web App project."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


##############################################################################
# Model definitions

class User(db.Model):
    """User of safe ride app."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(75))
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40))

    rating = db.relationship("Ratings")

    def __repr__(self):
        """Provide helpful representation when printed"""

        return "<User user_id=%s email=%s password=%s first_name=%s\
                last_name=%s>" % (self.user_id,
                                  self.email,
                                  self.first_name,
                                  self.last_name)


class Driver(db.Model):
    """Driver of safe ride app."""

    __tablename__ = "drivers"

    driver_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    zipcode = db.Column(db.Integer)
    driver_fname = db.Column(db.String(75))
    driver_lname = db.Column(db.String(75))
    driver_gender = db.Column(db.String(75))
    company = db.Column(db.String(75))
    green_star = db.Column(db.Boolean)

    rating = db.relationship("Ratings")

    def __repr__(self):
        """Provide helpful representation when printed"""

        return "<Driver driver_id=%s zipcode = %s driver_fname=%s driver_lname=%s\
        driver_gender=%s company=%s green_star=%s>" % (self.driver_id,
                                                       self.zipcode,
                                                       self.driver_fname,
                                                       self.driver_lname,
                                                       self.driver_gender,
                                                       self.company,
                                                       self.green_star)


class Ratings(db.Model):
    """Ratings for drivers"""

    __tablename__ = "ratings"

    ratings_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    driver_id = db.Column(db.Integer, db.ForeignKey("drivers.driver_id"))
    rating = db.Column(db.Integer)
    punctuality = db.Column(db.Integer)
    drop_off = db.Column(db.Boolean)
    special_instructions = db.Column(db.Boolean)
    feel_safe = db.Column(db.Boolean)
    driving_reckless = db.Column(db.Integer)
    harassment = db.Column(db.Boolean)
    comments = db.Column(db.String(1000))

    user = db.relationship("User")
    driver = db.relationship("Driver")

    def __repr__(self):
        """Provide helpful representation when printed"""

        return "<Ratings rating_id=%s user_id=%s driver_id=%s rating=%s\
        punctuality=%s drop_off=%s special_instructions=%s feel_safe=%s\
        driving_reckless=%s harassment=%s comments=%s>" % (self.rating_id,
                                                           self.user_id,
                                                           self.driver_id,
                                                           self.rating,
                                                           self.punctuality,
                                                           self.drop_off,
                                                           self.special_instructions,
                                                           self.feel_safe,
                                                           self.driving_reckless,
                                                           self.harassment,
                                                           self.comments)


##############################################################################
# Helper functions


def connect_to_db(app, db_uri="postgresql:///rides"):
    """Connect the database to our Flask app."""

    # Configure to use PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if you run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."
