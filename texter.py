
text  = text.split("\n")
name, img, short = name.split("(*)")
end_text = ""
for i in text:
    end_text += "<p>" + i + "</p><br>"


text = """<br>
            <img src="/static/img/2.jpeg" id="img_human" style="width: 39px; height: 39px; border-radius: 20px;" >
           <a href="/">
            <span class="human">
            HUMAN
            </span>
</a>
            <span>      5 д</span>
          <a href="/">
            <img src="/static/img/i (1).webp" style="height: 30px; width: 33px;float:right;margin-right: 5%;">
            </a>

            <br>
      
            <span class="article_name">
<h3>{0}</h3>
             </span>
           <br>
            <img src="{1}" style="width:100%; height: auto;border-radius: 20px;">
            <br>
            <br>
            <span class="article_text" style="font-family:cursive;text-align:center;">Схема ядерной батарейки</span>

            <br>
          <br>
          <br>
            <span class="article_text">
{2}
</span>
            <br>
            
            <br>
            <span class="views_num">6 k</span><span class="views">Показов</span>
            <img src="/static/img/soc_networks.jpg" style="width:120px; height: 40px;float:right;margin-right: 5%;">
            <br>
            <br>
""".format(name, img, end_text)
