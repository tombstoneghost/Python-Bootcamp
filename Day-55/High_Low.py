# Imports
from random import randint
from flask import Flask

# Flask Configurations
app = Flask(__name__)

# Globals
correct_number = randint(0, 9)

# Index Route
@app.route('/')
def index():
    content = '''
    <h1>Guess a number between 0 and 9</h1>
    <br/>
    <img src="https://i.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.webp" alt="GIF" />
    '''
    return content

# Number Route
@app.route('/<number>')
def guess(number):
    num = int(number)
    if num == correct_number:
        return '''
            <h1 style="color: green">You found me!</h1>
            <img src="https://i.giphy.com/media/4T7e4DmcrP9du/giphy.webp" alt="GIF" />
        '''
    elif num < correct_number:
        return '''
            <h1 style="color: red">Too Low, Try Again!</h1>
            <img src="https://i.giphy.com/media/jD4DwBtqPXRXa/giphy.webp" alt="GIF" />
        '''
    elif num > correct_number:
        return '''
            <h1 style="color: purple">Too High, Try Again!</h1>
            <img src="https://i.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.webp" alt="GIF" />
        '''

# Main
if __name__ == "__main__":
    app.run(debug=True)
