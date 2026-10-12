from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    count = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Staff %r>" % self.id


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")  





@app.route("/calculator", methods=["GET", "POST"])
def calculator():     
    result = None
    if request.method == "POST":
        expression = request.form.get("expression")
        try:
            result = eval(expression)
        except:
            result = f"Ошибка: "
    return render_template("calculator.html", result=result)  


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5001, debug=True)