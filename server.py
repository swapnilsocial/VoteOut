from flask import Flask, render_template

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return render_template('index.html')

@app.route('/vote/pets')
def vote_pets():
    return render_template('pets.html')

@app.route('/serverstatus')
def serverstatus():
    return "Server is running!"
app.run(debug=True)