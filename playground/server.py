from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play/')
def level_one():
    return render_template('index.html', num = 3, color = "#9ec5f8")

@app.route('/play/<int:x>')
def level_two(x):
    return render_template("index.html", num = x, color = "#9ec5f8")

@app.route('/play/<int:num>/<string:color>')
def level_three(num, color):
    return render_template("index.html", num = num, color = color)

if __name__ == "__main__":
    app.run(debug = True, port = 5001)

