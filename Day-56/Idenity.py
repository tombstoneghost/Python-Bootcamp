# Imports
from flask import Flask, render_template


# Flask Configurations
app = Flask(__name__)


# Index Route
@app.route("/")
def index():
    return render_template("index.html")



# Main
if __name__ == "__main__":
    app.run(debug=True)
