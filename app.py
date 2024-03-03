from flask import Flask, render_template, redirect, url_for, request, session
from db import get_all_news, get_news_by_id, add_news
app = Flask(__name__, template_folder='', static_folder='')

news = ['kdsfins', 'qwmdsffodsf', 'qwe121233', 'qwe123']
news_id = ['0','1','2','3']

data = [
    {
        "id": '0',
        "title": 'News',
        "content": "contetnt"
    },
    {
        "id": '1',
        "title": 'News 2',
        "content": "contetnt 2"
    }
]

@app.route("/")
def index():
    news =get_all_news()
    table_data = [
        (1, 1, 'name of command', 100),
        (2, 2, 'name of command 2', 50),
        (3, 3, 'name of command 3', 40),
    ]
    return render_template('home.html', news=news, table_data=table_data)


@app.route("/home/<id>")
def home(id):
    news = get_news_by_id(id)

    if news:
        return render_template('news.html', showed_news=news)

    
    return redirect('/')


@app.route("/auth/sign-in", methods=["GET", "POST"])
def signIn():
    if request.method == "POST":
        if request.form['username'] == 'color' and request.form['password'] == '#ffff':
            session['user'] = True
            session['inccorect_pass'] = False
            return redirect('/profile')
        else:
            session['inccorect_pass'] = True
            return redirect(url_for('signIn'))
            
    if ('inccorect_pass' in session.keys()  ):
        return render_template('sign-in.html', incorrect_password=session['inccorect_pass'])
    
    return render_template('sign-in.html', incorrect_password=False)

@app.route("/auth/sign-up")
def signUp():
    return render_template('sign-in.html')

@app.route("/profile", methods=["GET", "POST"])
def Profiler():
    if 'user' in session.keys() and session['user']:
        if request.method == "POST":
            add_news(request.form['title'], request.form['description'], request.form['imgUrl'])
        return render_template('profile.html')
    else:
        return redirect(url_for('signIn'))

app.secret_key = 'secret'

app.run(debug=True)
