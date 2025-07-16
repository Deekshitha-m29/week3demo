from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def index():
    return render_template("Form.html")

@app.route('/submit',methods=['POST'])
def submit():
    username=request.form['username']
    year=request.form['year']
    return render_template('Result.html',name=username,year=year)
if __name__=='__main__':
    app.run(debug=True)