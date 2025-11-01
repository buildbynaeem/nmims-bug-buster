# Your main Flask application (backend logic, API routes)
from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

