import os
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'symphony_massive_matrix_2026')

@app.route('/')
def index():
    return render_template('index.html')

# This block handles local running, while Render will use gunicorn instead
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)