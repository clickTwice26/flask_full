from flask import Flask, render_template, request, redirect

tutorial_link="https://www.youtube.com/watch?v=0Qxtt4veJIc&list=PLCC34OHNcOtolz2Vd9ZSeSXWc8Bq23yEz"
app = Flask(__name__) #helps find all of our files and directory
# Create a route decorator

@app.route("/")
def index():
    first_name = "John"
    stuff = "This is <strong> Bold </strong>"
    item_list = ["item1", "item2", "item3", 41, 41]
    return render_template("index.html", first_name=first_name, stuff=stuff, item_list=item_list)
@app.route("/user")
def user():
    return render_template("user.html")
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404
@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500
if __name__ == "__main__":
    app.run(debug=True)