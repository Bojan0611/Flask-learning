from app import app

from datetime import datetime
from flask import render_template, request, redirect

@app.template_filter("clean_date")
def clean_date(dt):
    return dt.strftime("%d %b %Y")

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/jinja")
def jinja():
    my_name = "Kuba"
    age = 27
    langs = ["Python", "JavaScript", "Ruby", "Java", "C"]
    friends = {
        "Tom": 30,
        "Amy": 45,
        "Tony": 23,
        "Clarissa": 18
    }
    colours = ("Red", "Green")
    cool = True
    class GitRemote:
        def __init__(self, name, description, url):
            self.name=name
            self.description=description
            self.url=url
            
        def pull(self):
            return f"pulling repo {self.name}"
        
        def clone(self):
            return f"cloning into {self.url}"
        
    my_remote = GitRemote("flask jinja", "temple design tutorial", "https://github.com/kuba/jinja.git")
    
    def repeat(x, qty):
        return x*qty
    
    date = datetime.utcnow()
    
    my_html = "<h1>THIS IS SOME HTML</h1>"
    
    suspicious = "<script>alert('you have got hacked!')</script>"
    
    return render_template("public/jinja.html", my_name=my_name, age=age,
                           langs=langs, friends=friends, colours=colours,
                           cool=cool, GitRemote=GitRemote, repeat=repeat,
                           my_remote=my_remote, date=date, my_html=my_html,
                           suspicious=suspicious)

@app.route("/about")
def about():
    return render_template("public/about.html")

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    
    if request.method == "POST":
        req = request.form
        print(req)

        return redirect(request.url)
    
    return render_template("public/sign_up.html")
