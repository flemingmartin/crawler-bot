from flask import Flask
from flask import render_template
import jyserver.Flask as jsf
import random
import time



app = Flask(__name__)

@jsf.use(app)
class App:
    def __init__(self):
        pass

    def step(self):
        for i in range(15):
            new_weights = random.sample(range(0, 10), 4)
            self.js.update_table(new_weights)
            time.sleep(0.5)

@app.route('/')
def index():
    return App.render(render_template('index.html'))

if __name__ == '__main__':
    app.run(debug=True)