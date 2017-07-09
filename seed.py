"""Utility - seeds tables."""

from sqlalchemy import func
from model import connect_to_db, db
from model import User, Driver, Ratings


def add_users():
    """Seed fake users to database"""

    for row in open("static/user.csv"):

        row = row.rstrip()
        first_name, last_name, email = row.split(",")

        user = User(first_name=first_name,
                    last_name=last_name,
                    email=email)

        db.session.add(user)

    db.session.commit()
    print "Done seeding users"


def add_drivers():
    """Seed fake drivers to database."""

    for row in open("static/driver.csv"):

        row = row.strip()
        zipcode, driver_fname, driver_lname, driver_gender, company, green_star = row.split(",")

        driver = Driver(zipcode=zipcode,
                        driver_fname=driver_fname,
                        driver_lname=driver_lname,
                        driver_gender=driver_gender,
                        company=company,
                        green_star=green_star)

        db.session.add(driver)

    db.session.commit()
    print "Done seeding drivers"


def add_ratings():
    """Seed fake ratings to database."""

    for row in open("static/rating.csv"):

        row = row.rstrip()
        user_id, driver_id, rating, punctuality, drop_off, special_instructions, feel_safe, driving_reckless, harassment, comments = row.split(",")

        rating = Ratings(user_id=user_id,
                         driver_id=driver_id,
                         rating=rating,
                         punctuality=punctuality,
                         drop_off=drop_off,
                         special_instructions=special_instructions,
                         feel_safe=feel_safe,
                         driving_reckless=driving_reckless,
                         harassment=harassment,
                         comments=comments)

        db.session.add(rating)

    db.session.commit()
    print "Done seeding ratings"


################################################################################
if __name__ == "__main__":

    from server import app
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()

    # add_users()
    # add_drivers()
    add_ratings()
