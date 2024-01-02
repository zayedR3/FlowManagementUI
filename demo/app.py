from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
   return render_template("test2.html")

if __name__ == '__main__':
   app.run(debug=True)

