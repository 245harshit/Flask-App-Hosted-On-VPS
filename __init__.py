from flask import Flask, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hais i*#) #*# #*(@9 iewd (2(((!9309-'

@app.route("/")  # this sets the route to this page
def home():
	return jsonify({'Message': "Testing"})

if __name__ == "__main__":
    app.run()
