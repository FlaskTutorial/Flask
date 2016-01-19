from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello_world(name=None):
  return render_template('layout.html', name=name)

@app.route('/home')
def home():
  return render_template('layout.html')

@app.route('/flask')
def flask():
  return render_template('flask.html')

if __name__ == '__main__':
  app.run()