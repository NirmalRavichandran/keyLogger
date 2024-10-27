
# **Python Keylogger**

## **Description**
This project is a simple Python keylogger that captures keystrokes on the client's device and sends the collected data to a remote server. The client-side script utilizes the `pynput` library to monitor keyboard inputs, while the server processes and stores the received keystrokes. The communication between client and server is authenticated using a token-based system to ensure secure data transfer.

## **Features**
- Captures regular keys and special keys (e.g., `Enter`, `Space`, `Shift`).
- Buffers keystrokes to minimize network requests.
- Securely transmits data to the server using an authentication token.
- Simple server setup to receive and log keystrokes.

## **Prerequisites**
- Python 3.x
- `pynput` library (for client)
- `Flask` library (for server)
- `requests` library (for client)

You can install the required libraries using:
```bash
pip install pynput flask requests
```

## **Setup**

### **Client**
1. Edit the client script (`client.py`) to set the `SERVER_URL` and `AUTH_TOKEN`.
2. Run the client script to start capturing keystrokes.
   ```bash
   python client.py
   ```

### **Server**
1. Edit the server script (`server.py`) to set the `AUTH_TOKEN`.
2. Run the server to start receiving data.
   ```bash
   python server.py
   ```

## **Usage**
1. Start the server by running `server.py` on the host machine.
2. Run `client.py` on the client machine to begin capturing and sending keystrokes.
3. The keystrokes will be logged on the server in a file named `keystrokes.txt`.

## **Security Note**
- This script is for educational purposes only. Ensure that you have permission before using it on any device.
- Misuse of keyloggers can violate privacy laws and regulations.
