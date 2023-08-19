from app import app


@app.route("/")
def hello_world():
    return "it works!"

if __name__== "__main__":
    app.run(debug=True)