from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template('layout.html')

@app.route('/home/')
@app.route('/home/<name>')
def home(name=None):
  return render_template('home.html', name=name)

@app.route('/flask')
def flask():
  return render_template('flask.html')

if __name__ == '__main__':
  app.run()