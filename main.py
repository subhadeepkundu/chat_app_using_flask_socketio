from flask import Flask, render_template, request
from flask_socketio import SocketIO, send
app=Flask(__name__)
app.config['SECRET_KEY']='difficult to guess'
socketio=SocketIO(app)

@app.route('/')
def index():
	return render_template('index.html')

@socketio.on('message')
def handleMessage(msg):
	print('Message: ' + msg)
	send(msg,broadcast=True)
if __name__=='__main__':
	socketio.run(app, debug=True)