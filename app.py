from flask import Flask, render_template,request,jsonify

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home_page():
    return render_template('index.html')

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

if __name__=="__main__":
    app.run(host="0.0.0.0")
