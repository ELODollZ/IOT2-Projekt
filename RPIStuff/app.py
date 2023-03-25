## Imports
from flask import Flask, render_template


app = Flask(__name__)


### Routes
@app.route('/')
def appMainpage():
    return render_template('mainPage.html')
if __name__ == '__main__':
    app.run()

