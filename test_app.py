from flask import Flask, render_template, redirect, url_for
import subprocess

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to trigger the Python script
@app.route('/run-script')
def run_script():
    # Run your Python script here
    # For demonstration, let's use a simple subprocess call
    subprocess.run(['python', 'QuickAgent.py'])
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
