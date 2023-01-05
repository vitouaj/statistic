from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('m4.html')

if __name__=='__main__':
 app.run(host='localhost',port=8080)

