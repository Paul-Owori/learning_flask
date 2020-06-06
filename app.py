from flask import Flask, render_template

# Create an instance of a flask app
app = Flask(__name__)

# Allow auto reloading by creating a debug environment
app.debug = True

# Routes

# Render string
# @app.route('/')
# def index():
#     return 'HELLO WORLDS'

# Render html


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


# Run the app if this file is the one being run
if __name__ == '__main__':
    app.run()
