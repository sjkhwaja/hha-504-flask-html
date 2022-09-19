from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
  return render_template('p1_homepage.html')

@app.route('/')
def page2():
  return render_template('p2_page2.html')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0'. port=80)
