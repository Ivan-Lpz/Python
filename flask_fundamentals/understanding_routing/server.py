from flask import Flask
app = Flask (__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojooooo!'

@app.route('/say/<names>')
def hi (names):
    return f"Hi {names}"

@app.route("/repeat/<phrase>/<int:times>")
def repeat_times(phrase,times):
    repeated = phrase * times
    return repeated

if __name__=="__main__":
    
    app.run(debug=True)

