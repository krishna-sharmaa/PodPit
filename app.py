from flask import Flask, render_template, request, send_file
from models import tts, script_gen

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form['user_input']
        # user_input+=". give lines for a pod
        print(user_input)
        script = script_gen.contentGenerator(user_input)
        print(script)
        tts.text_to_speech(script)
        return render_template('results.html')
    return render_template('index.html')

@app.route('/download')
def download():
    path_to_file = "result.mp3"
    return send_file(path_to_file, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)