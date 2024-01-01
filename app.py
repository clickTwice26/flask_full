from flask import Flask, render_template, request, redirect



app = Flask(__name__) #helps find all of our files and directory



# Create a route decorator

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/user/<username>")
def user(username):
    return f"<h1>{username}</h2>"

if __name__ == "__main__":
    app.run(debug=True)