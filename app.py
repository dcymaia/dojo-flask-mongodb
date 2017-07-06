from flask import Flask, render_template
from flask_pymongo import PyMongo

my_app_web = Flask('my_app_web')
my_mongo = PyMongo(my_app_web)


@my_app_web.route('/')
def home_page():
    online_users = my_mongo.db.users.find({'online': True})
    return render_template('index.html',
                           online_users=online_users)


@my_app_web.route('/user/<username>')
def user_profile(username):
    user = my_mongo.db.users.find_one_or_404({'_id': username})
    return render_template('user.html',
                           user=user)


if __name__ == "__main__":
    my_app_web.run()
