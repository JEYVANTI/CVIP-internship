import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    print("Current working directory:", os.getcwd())
    templates_path = os.path.join(os.getcwd(), 'templates')
    print("Template folder path:", templates_path)
    print("Template folder contents:", os.listdir(templates_path))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
