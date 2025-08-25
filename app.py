from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/stillDeveloping.html")
def still_developing():
    return render_template("stillDeveloping.html")
    
@app.route("/origami")
def origami():
    return render_template("origami.html")
    
if __name__ == "__main__":
    app.run()
