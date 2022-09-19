from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def homepage():
  return render_template('p1_homepage.html')

@app.route('/page2')
def page2():
 return render_template('p2_page2.html')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=80)
