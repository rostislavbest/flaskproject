from flask import Flask, render_template,redirect,request
from random import randint
app = Flask(__name__)
data_main = []
@app.route("/")
def home():
    num = 99
    return render_template("index.html",data_main = data_main,num = num)


@app.route("/about",methods = ["GET","POST"])
def about():
    data = "якась інформація"
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        color = request.form["color"]
        id  = randint(1,1000000000)
        data_main.append({'name':name,'age':age,'color':color,'id':id})
    return render_template("about.html", data = data)


@app.route("/delete/<int:id>",methods = ["GET","POST"])
def del_data(id):
    item_to_del = None
    # item_to_del = next(item for item in data_main if item['id'] == id)
    for el in data_main:
        if el['id'] == id:
            item_to_del = el
            break
   
    data_main.remove(item_to_del)
    return redirect("/")


if __name__ == "__main__":

    app.run()




# git init
# git add .
# git commit -m "initial commit"
# 

# git branch -M main
# git remote add origin https://github.com/ТВОЄ_ІМ'Я/my-flask-app.git
# git push -u origin main