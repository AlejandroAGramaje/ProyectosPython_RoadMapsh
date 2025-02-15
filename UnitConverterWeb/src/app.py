from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/Length')

def length():
    return render_template("Length.html")
@app.route('/weight')

def weight():
    return render_template("weight.html")

@app.route('/temperature')
def temperature():
    return render_template("temperature.html")


if __name__ == '__main__':
    app.run(debug=True)