import os
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")                           
def about_member(member_name):
    member = {}
    
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
                
            return render_template("member.html", member=member)


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True) 
            
            
            
            
            
            
            
"""
Reading From A JSON File
https://www.youtube.com/watch?v=fzP0Y-Z6E2M

Iterating Over Our JSON Data
https://www.youtube.com/watch?v=r1fo9iN8cfM

Using If Statements Inside Our HTML
https://www.youtube.com/watch?v=ooIRblr0BVc

Advanced Routing
https://www.youtube.com/watch?time_continue=26&v=x8VY_2A8ze4

"""