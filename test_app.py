# Author: Brandon Bayquen
# Last modified: 8/1/2024 @ 1pm KST (South Korea)

from flask import Flask, render_template, redirect, url_for
import subprocess

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('indextest1.html')

# Route to trigger the Python script
@app.route('/run-script')
def run_script():
    # Run your Python script here
    # For demonstration, let's use a simple subprocess call
    subprocess.run(['python', 'QuickAgent.py'])
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
