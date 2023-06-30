from flask import Flask, render_template, session, redirect

app = Flask (__name__)

app.secret_key = " my first secret key"

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 0
    else:
        session['count'] += 1
    return render_template("index.html")

@app.route('/add2')
def add2():
    session["count"] +=1
    return redirect('/')

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True, port = 5001 )