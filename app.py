from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
tutorial_link="https://www.youtube.com/watch?v=0Qxtt4veJIc&list=PLCC34OHNcOtolz2Vd9ZSeSXWc8Bq23yEz"
app = Flask(__name__) #helps find all of our files and directory
app.config['SECRET_KEY'] = 'chipichipichapachapadubidubudabadaba'

# Create a Form Class
class NamerForm(FlaskForm):
    name = StringField("What's your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")# Create a route decorator
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
    form = NamerForm()
    #validate form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template("name.html", name=name, form=form)



if __name__ == "__main__":
    app.run(debug=True)