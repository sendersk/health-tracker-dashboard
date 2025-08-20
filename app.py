from flask import Flask, render_template, request, redirect, url_for
from forms import HealthDataForm

app = Flask(__name__)

# define homepage route and index() view function
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['POST', 'GET'])
def form():
    form = HealthDataForm()
    if request.method == 'POST':
        # process form data here
        return redirect(url_for('dashboard'))
    return render_template('form.html', form=form)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)