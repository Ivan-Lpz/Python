from flask import Flask, render_template

app = Flask (__name__)

# @app.route('/play')
# def index ():
#     return render_template("index.html")

# @app.route('/play/<int:times>') #creating a variable times which will be taken in as an integer
# def boxtimes(times):                        #"boxtimes is the name of the function"it can be anyting
#     return render_template("index.html", times = times)  #green variable effects the html and should have the same name

@app.route('/play/<int:times>/<color>')             #alligator mouth makes this <color> a variable
def boxcolor(times,color):
    return render_template("index.html", times = times, color = color)


if __name__=="__main__":

    app.run(debug=True)