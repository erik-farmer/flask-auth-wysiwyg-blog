from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

admin = Admin(app, name='microblog', template_mode='bootstrap3')

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    body = db.Column(db.Text())

    def __repr__(self):
        return '<Post %r>' % self.title

db.create_all()

admin.add_view(ModelView(Post, db.session))

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.debug = True
    app.run()