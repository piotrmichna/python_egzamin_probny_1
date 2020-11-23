from flask import Flask, render_template, request
import exam

app = Flask('Movie')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


app.run(debug=True)

