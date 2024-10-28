from flask import Flask, render_template, request
import re
app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    return render_template("hello.html", name=input_name, age=input_age)


@app.route("/query", methods=["GET"])
def process_queries():
    query = request.args.get("q", "")
    return process_query(query)


def process_query(query):
    if query == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    elif "your name" in query:
        return "yfwt"
    elif "Which of the following numbers is the largest" in query:
        numbers = re.findall(r'\d+', query)
        number_list = [int(num) for num in numbers]
        return max(number_list)
    elif "plus" in query:
        numbers = re.findall(r'\d+', query)
        number_list = [int(num) for num in numbers]
        return sum(number_list)
    else:
        return "Unknown"
