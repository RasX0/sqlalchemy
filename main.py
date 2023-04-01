from data import db_session
from data.users import User
from data.jobs import Jobs
import datetime
from flask import Flask, redirect
from flask import url_for, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

file_name = input()
db_session.global_init(f"db/{file_name}")

db_sess = db_session.create_session()
for i in range(1, len(db_sess.query(Jobs).all()) + 1):

    user = db_sess.query(User).filter(User.id == i).first()
    print(user)


@app.route('/')
@app.route('/index')
def index():
    users = "Ученик Яндекс.Лицея"
    return render_template('index.html', title='Домашняя страница',
                           username=users)


@app.route('/workslog')
def workslog():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs)
    db_sess1 = db_session.create_session()
    user = db_sess1.query(User)
    return render_template('WorksLog.html', jobs=jobs, user=user)


# cap = Jobs(team_leader=3, job='Development of a management system', work_size=25, collaborators='5',
#            is_finished=False)
# db_sess1 = db_session.create_session()
# db_sess1.add(cap)
# db_sess1.commit()

# db_sess1.add(captain)
# db_sess1.commit()
#
# cleaner = User(surname="Цуров", name="Анри", age=15, position="cleaner", speciality="deck cleaner",
#                address="module_2", email="astroworld@mars.org")
# db_sess2 = db_session.create_session()
# db_sess2.add(cleaner)
# db_sess2.commit()
#
# manager = User(surname="Михаил", name="Волобой", age=25, position="manager", speciality="senior manager",
#                address="module_3", email="school37@mars.org")
# db_sess = db_session.create_session()
# db_sess.add(manager)
# db_sess.commit()

# user = User()
# user.name = "Пользователь 1"
# user.about = "биография пользователя 1"
# user.email = "email@email.ru"
# db_sess = db_session.create_session()
# db_sess.add(user)
# db_sess.commit()
# user2 = User()
# user2.name = "Пользователь 2"
# user2.about = "биография пользователя 2"
# user2.email = "email2@email.ru"
# db_sess = db_session.create_session()
# db_sess.add(user2)
# db_sess.commit()
# app.run()


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
