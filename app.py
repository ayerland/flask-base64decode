import re
import base64
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "super-secret-flask-key-e3b0c44298fc1c149afbf4c8996fb9"


def base64_decode(base64_text):
    decoded_data = None
    decoded_data = base64.urlsafe_b64decode(base64_text)
    return str(decoded_data.decode('utf-8'))


@app.route("/", methods=['POST', 'GET'])
def process():
    output = None
    entry = None
    try:
        entry = str(request.form['64base_decode'])
    except Exception as e:
        pass

    if entry:
        try: 
            if entry:
                try:
                    output = base64_decode(entry)
                    flash(output)

                except Exception as e:
                    flash(e)
                    pass
            else:
                flash('Invalid entry!')
      
        except Exception as e:
            flash(e)
            pass

    return render_template("index.html")


