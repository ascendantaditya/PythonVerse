from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_guess', methods=['POST'])
def check_guess():
    secret_name = "Elon Musk"
    guess = request.form.get('guess')

    if guess == secret_name:
        result_message = "You Win!"
        color = "green"
    else:
        result_message = "Try again. Incorrect guess."
        color = "red"

    return render_template('index.html', result_message=result_message, color=color)

if __name__ == '__main__':
    app.run(debug=True)
