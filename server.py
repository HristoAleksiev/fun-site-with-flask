from flask import Flask
import random as r

app = Flask(__name__)
random_number = r.randint(0, 9)


@app.route("/")
def hello():
    return "<h1>Guess a number between 0 and 9: </h1>" \
           "<img src='https://media.giphy.com/media/xUn3CftPBajoflzROU/giphy.gif' />"


@app.route("/<int:number>")
def check_guess(number):
    if number == random_number:
        return "<h1 style='color: green'>That was the correct number!! :)</h1>"
    elif number > random_number:
        return "<h1 style='color:red'>Your answer is too high! :(</h1>"
    elif number < random_number:
        return "<h1 style='color:blue'>Your answer is too low!</h1>"


if __name__ == "__main__":
    app.run(debug=True)

