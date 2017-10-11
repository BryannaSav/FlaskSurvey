from flask import Flask, request, redirect, render_template, session, flash
app=Flask(__name__)
app.secret_key=("keykey")
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/result', methods=["POST"])
def result():
    if len(request.form['name'])<1 or len(request.form['comments'])<1:
        flash("Name and Comment cannot be left blank")
        return redirect('/')
    elif len(request.form['comments'])>120:
        flash("Comments must be shorter that 120 characters")
        return redirect('/')
    else:
        return render_template('result.html', name=request.form['name'], location=request.form['location'], language=request.form['language'], comments=request.form['comments'])
@app.route('/goback')
def goback():
    return redirect('/')
app.run(debug=True)
