from flask import Flask, render_template, request, redirect
from subjectHandler import SubjectHandler
from contentHandler import ContentHandler
import os 

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
    if not args:
        return redirect('/')
    print(args)
    if 'subject' in args and 'primer' in args:
        path = os.path.join(args['subject'], args['primer'] + '.md')
    else:
        return redirect('/')
    ch = ContentHandler(path)
    
    try:
        content = ch.get_HTML()
    except:
        return redirect('/')
    else:
        return render_template('read.html', content = content)

if __name__ == "__main__":
    app.run(port=8000)