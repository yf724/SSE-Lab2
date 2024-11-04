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


@app.route("/github", methods=["POST"])
def github():
    return "hello"


def process_query(query):
    if query == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    elif "your name" in query:
        return "yfwt"
    elif "Which of the following numbers is the largest" in query:
        numbers = re.findall(r'\d+', query)
        number_list = [int(num) for num in numbers]
        return str(max(number_list))
    elif "plus" in query:
        numbers = re.findall(r'\d+', query)
        number_list = [int(num) for num in numbers]
        return str(sum(number_list))
    elif "multiplied" in query:
        numbers = re.findall(r'\d+', query)
        number_list = [int(num) for num in numbers]
        return str(number_list[0] * number_list[1])
    elif "a square and a cube" in query:
        numbers = re.findall(r'\d+', query)
        number_list = [int(num) for num in numbers]
        answer = []
        for i in range(7):
            if number_list[i]**(1/2) == round(number_list[i]**(1/2)):
                if cube(number_list[i]):
                    answer.append(str(number_list[i]))
        return answer
    elif "primes" in query:
        numbers = re.findall(r'\d+', query)
        number_list = [int(num) for num in numbers]
        answer = []
        for i in range(5):
            if primes(number_list[i]):
                answer.append((number_list[i]))
        answer.sort()
        answers = []
        for item in answer:
            answers.append(str(item))
        return ", ".join(answers)
    elif "minus" in query:
        numbers = re.findall(r'\d+', query)
        number_list = [int(num) for num in numbers]
        return str(number_list[0] - number_list[1])
    elif "power" in query:
        numbers = re.findall(r'\d+', query)
        number_list = [int(num) for num in numbers]
        return str(number_list[0] ** number_list[1])
    else:
        return "Unknown"


def cube(num):
    for i in range(num):
        if i**3 == num:
            return True
    return False


def primes(num):
    for i in range(2, num):
        if (num / i) == round(num / i):
            return False
    return True
