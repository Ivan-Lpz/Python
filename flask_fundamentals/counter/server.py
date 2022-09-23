from flask import Flask, render_template, redirect, session
app = Flask (__name__)
app.secret_key = 'secret'

@app.route("/")
def main():
    if "increment" not in session:
        session ["increment"] = 0

    counter = session["increment"] 
    counter += 1
    session["increment"] = counter

        
    return render_template("counter.html")

@app.route("/clear")
def reset():
    session.clear()
    
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)