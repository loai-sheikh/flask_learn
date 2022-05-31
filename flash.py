from flask import Flask, flash, redirect, url_for, render_template, request
# initialaize the flask application
app = Flask(__name__)
app.secret_key = 'RL9hdrZN4I'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid username or password. please try again!'
            return render_template('log_in.html', error=error)
        else:
            flash('You were successfully logged in')
            flash('logout before login again')
            return redirect(url_for('index'))
    else:
        return render_template('log_in.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)
