from flask import Flask, render_template, redirect, url_for

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
    return render_template('home.html', news=data)


@app.route("/home/<id>")
def home(id):
    
    for news in data:
        if news['id'] == id:
            return render_template('news.html', showed_news=news, ids=news_id)

    
    return redirect('/')


app.run(debug=True)
