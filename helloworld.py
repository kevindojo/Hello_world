from flask import Flask, render_template            # watch capitalization
app = Flask(__name__)                               #watch Capitalization

@app.route('/')

def hello_world():
    return render_template('index.html')

app.run(debug=True)