from flask import Flask, render_template, request
from main import unit_converter
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/length', methods=['GET', 'POST'])
def length():
    if request.method == 'POST':
        value = float(request.form['value'])
        unit_from = request.form['unit_from']
        unit_to = request.form['unit_to']
        result = unit_converter(value, unit_from, unit_to)
        return render_template('result.html', value=value, unit_from=unit_from, unit_to=unit_to, result=result, category="Length")
    return render_template('length.html')

@app.route('/weight', methods=['GET', 'POST'])
def weight():
    if request.method == 'POST':
        value = float(request.form['value'])
        unit_from = request.form['unit_from']
        unit_to = request.form['unit_to']
        result = unit_converter(value, unit_from, unit_to)
        return render_template('result.html', value=value, unit_from=unit_from, unit_to=unit_to, result=result, category="Weight")
    return render_template('weight.html')

@app.route('/temperature', methods=['GET', 'POST'])
def temperature():
    if request.method == 'POST':
        value = float(request.form['value'])
        unit_from = request.form['unit_from']
        unit_to = request.form['unit_to']
        result = unit_converter(value, unit_from, unit_to)
        return render_template('result.html', value=value, unit_from=unit_from, unit_to=unit_to, result=result, category="Temperature")
    return render_template('temperature.html')

if __name__ == '__main__':
    app.run(debug=True)