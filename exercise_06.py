from flask import Flask, render_template, request
import exam

app = Flask('Movie')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/movies', methods=['GET', 'POST'])
def movies():
    if request.method == 'GET':
        return render_template('movies.html', title='', result='')
    else:
        if request.form["title"] == '':
            return render_template('movies.html', title=request.form["title"], result='Empty title!')
        else:
            if request.form["title"] in exam.movies['favourite']:
                result = 'favourite'
            elif request.form["title"] in exam.movies['hated']:
                result = 'hated'
            else:
                result = 'no such movie!'

        return render_template('movies.html', title=request.form["title"], result=result)


app.run(debug=True)

