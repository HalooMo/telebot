import requests
import sys
sys.path.append(r'C:\Users\salim\GetFiles')
import texter, texter_result 

URI = "https://jaconda.online"

def get_file():
    name_list = []
    file = input('Эээ, введите путь к файлу  ')
    with open(file, "r") as f:
        for i in f.readlines():
            name_list.append(i)
    return name_list


def request_article(article_generator, name_list):
    for text, name in zip(list(article_generator), name_list):
        ARTICLE_TEXT_BASE = """
<br>
            <img src="/static/img/Carlos Sainz.jpeg" id="img_human" style="width: 39px; height: 39px; border-radius: 20px;" >
           <a href="/">
            <span class="human">
            HUMAN
            </span>
</a>
            <span>      5 д</span>
            <a href="/">
            <img src="/static/img/i (1).webp" style="height: 30px; width: 33px;margin-left: 56%;">
            </a>
            <br>
            <span class="article_name"><h3>{0}</h3></span>
            <br>
            <span class="article_text">
                {i}
            </span>
            <br>
            <br>
            <br>
            <br>
            <span class="views_num">6 k</span><span class="views">Показов</span>
            <img src="/static/img/soc_networks.jpg" style="width:120px; height: 40px; margin-left: 265px;">
            <br>
            <br>
""".format(name, text)
        playload = {"name":name, "text":text, "categoty":"INV"}
        s = requests.request("POST", url=URL, params=playload)



request_article(texter_result.get_article(texter.text_generation(get_file())), get_file())