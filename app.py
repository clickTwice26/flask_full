from flask import Flask, render_template, request, redirect,flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
tutorial_link="https://www.youtube.com/watch?v=0Qxtt4veJIc&list=PLCC34OHNcOtolz2Vd9ZSeSXWc8Bq23yEz"
app = Flask(__name__) #helps find all of our files and directory
app.config['SECRET_KEY'] = 'chipichipichapachapadubidubudabadaba'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Add database(old.1)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# New Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password123@localhost/our_users'
# Initialize the Database
db = SQLAlchemy(app)



app.app_context().push()
# Create Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    date_added = (db.Column(db.DateTime, default=datetime.utcnow()))

    # Create a string
    def __repr__(self):
        return '<Name %r>' % self.name


# Create a Form Class
class UserFrom(FlaskForm):
    name = StringField("Name here", validators=[DataRequired()])
    email = StringField("Email here", validators=[DataRequired()])

    submit = SubmitField("Submit")# Create a route decorator


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id:int):
    form = UserFrom()
    name_to_update = User.query.get_or_404(id)
    if request.method == 'POST':
        name_to_update.name = request.form['name']
        name_to_update.email = request.form['email']
        try:
            db.session.commit()
            flash('User update Successful!', 'success')
            return render_template("update.html", form=form, name_to_update=name_to_update)
        except:
            flash('Looks like there was a problem. Try again!', 'success')
            return render_template("update.html", form=form, name_to_update=name_to_update)
    else:
        # flash('Looks like there was a problem. Try again!', 'success')
        return render_template("update.html", form=form, name_to_update=name_to_update)
@app.route("/user/add", methods=['GET', 'POST'])    
def add_user():
    name = None
    form = UserFrom()

    if form.validate_on_submit():
        # print(type(form.name.data))
        # print(type(form.email.data))
        # return "None"
        user = User.query.filter_by(email=str(form.email.data)).first()

        if user is None:
            user = User(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name =form.name.data
        form.name.data = ''
        form.email.data = ''
        flash("User Added Successfully")
    our_users = User.query.order_by(User.date_added)
    return render_template("add_user.html", form=form, name=name, our_users=our_users)

@app.route("/")
def index():

    first_name = "John"

    stuff = "This is <strong> Bold </strong>"
    item_list = ["item1", "item2", "item3", 41, 41]
    return render_template("index.html", first_name=first_name, stuff=stuff, item_list=item_list)
@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404
@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500


#create name page
@app.route("/name", methods=["GET", "POST"])
def name():
    name = None
    form = UserFrom()
    #validate form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form Submitted Successfully")
    return render_template("name.html", name=name, form=form)



if __name__ == "__main__":
    app.run(debug=True)