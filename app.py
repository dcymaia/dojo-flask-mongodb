from flask import Flask, render_template
from flask_pymongo import PyMongo

my_app_web = Flask('my_app_web')
my_mongo = PyMongo(my_app_web)


@my_app_web.route('/')
def home_page():
    online_users = my_mongo.db.users.find({'online': True})
    return render_template('index.html',
                           online_users=online_users)


@my_app_web.route('/list')
def list_machine():
    return render_template('list_machine.html')


if __name__ == "__main__":
    my_app_web.run()
