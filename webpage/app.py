from flask import Flask, render_template, request
import subprocess
import threading
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('control.html')

@app.route('/start_program', methods=['POST'])
def start_program():
    # Start the program in a separate thread
    threading.Thread(target=run_program).start()
    return 'Program started'

def run_program():
    subprocess.run(['python', 'every3.py'])
    # Sleep for 5 minutes then stop the program
    time.sleep(300)
    # Stop the program (assuming it's a process you can terminate)
    # Add code here based on how you would stop the program
    print("Program stopped")

if __name__ == '__main__':
    app.run(debug=True)
