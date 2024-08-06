from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "hi"

if __name__== "__main__":
    print("starting python flask server for House price prediction.... ")
    app.run()  
