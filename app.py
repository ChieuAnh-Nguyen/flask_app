
from flask import Flask, render_template


posts = [
    {
        "user": "Bob",
        "message": "hey"

    },
    {
        "user": "Mary",
        "message": "sup"
    }
]
app = Flask(__name__)

@app.route("/")
@app.route("/home")

# about.html uses the posts variable on the left, which is assigned posts created up top'''
def home():
    return render_template("layout.html")

@app.route('/about')
def about():
    return render_template("about.html", posts = posts)

if __name__ == '__main__':
    app.run(debug=True)
