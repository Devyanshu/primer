from flask import Flask, render_template, request
from subjectHandler import SubjectHandler

app = Flask(__name__, static_url_path='/static')

app.debug = True
app.secret_key = "nothingfornow"




@app.route("/")
def home():
    sh = SubjectHandler()
    subjects = sh.subjects
    primers = {}
    for ii in subjects:
        topics = sh.get_primers(ii)
        if topics:
            primers[ii] = topics
    return render_template('index.html', data=primers)


@app.route("/read")
def read():
    args = dict(request.args)
    print(args)
    return render_template('read.html')

if __name__ == "__main__":
    app.run(port=8000)