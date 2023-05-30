from flask import Flask,render_template,request
from datetime import datetime
import json,os

app = Flask(__name__)

get_cwd = os.getcwd()
if 'aboutmusic' in get_cwd:
    get_cwd += '/mysite'
    
with open(get_cwd+'/instruments.json','r') as file:
    instruments = json.load(file)

@app.template_filter()
def reading_time(para_word_count):
    reading_time_user = 250
    return para_word_count / reading_time_user

@app.route("/")
def index():
    name = 'Kyra'
    return render_template("index.html",instruments=instruments,name=name)

@app.route("/about")
def about():
    return render_template("aboutus.html")

@app.route("/calculation",methods=['GET','POST'])
def calculate():
    addition = None
    if request.method == 'POST':
        num = int(request.form["num"])
        num1 = int(request.form["num1"])
        addition = num + num1
    name = 'Kyra'
    time = datetime.now().strftime(('%d-%b-%Y %H:%M:%S %p'))
    para = 'adipisicing elit. Eos voluptatem delectus explicabo laboriosam reiciendis saepe itaque distinctio minima placeat nulla veniam optio rerum laborum, amet dignissimos. Et nihil ipsum excepturi.adipisicing elit. Eos voluptatem delectus explicabo laboriosam reiciendis saepe itaque distinctio minima placeat nulla veniam optio rerum laborum, amet dignissimos. Et nihil ipsum excepturi.adipisicing elit. Eos voluptatem delectus explicabo laboriosam reiciendis saepe itaque distinctio minima placeat nulla veniam optio rerum laborum, amet dignissimos. Et nihil ipsum excepturi.adipisicing elit. Eos voluptatem delectus explicabo laboriosam reiciendis saepe itaque distinctio minima placeat nulla veniam optio rerum laborum, amet dignissimos. Et nihil ipsum excepturi.adipisicing elit. Eos voluptatem delectus explicabo laboriosam reiciendis saepe itaque distinctio minima placeat nulla veniam optio rerum laborum, amet dignissimos. Et nihil ipsum excepturi.'
    reading_time = 250
    return render_template("calculation.html", name = name, time=time, para=para, reading_time=reading_time, addition=addition)

@app.template_filter()
def greeting(name):
    hour = datetime.now().hour
    if hour > 1 and hour < 12:
        return f"Good Morning {name}"
    elif hour > 11 and hour < 16:
        return f"Good Afternoon {name}"
    else:
        return f"Good Evening {name}"

if __name__ == '__main__':
    app.run(debug=True)