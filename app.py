from flask import Flask, request, jsonify, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.j2")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444, debug=True)

