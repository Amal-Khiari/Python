from flask import Flask , render_template

# Instance of flask 
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/home")
def home():
    return render_template("home.html")

#print(__name__)

#print("this is inside the server.py")

#if __name__ == "__main__":
    #print("this file was executed directly")
#else:
    #print(f"this file was executed as module({__name__}.js)")  
print("1 2 3 4 ")  

if __name__ == "__main__":
    app.run(debug=True)

