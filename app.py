from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
@app.route('/', methods=["GET", "POST"])

def index():

    linux_news_url = "https://www.linuxtoday.com/news/"
    req_hook = requests.get(linux_news_url)
    soup = BeautifulSoup(req_hook.content,"html.parser")
    final_ln=""
    boilerplate = soup.find_all("div", class_ = "td-module-meta-info", limit=8)
    for data in boilerplate:
        linux_news = data.h3.a['title']
        final_ln += "\u2022 " + linux_news + "\n"
        # print(final_ln)
    return render_template("index.html", news_linux=final_ln)