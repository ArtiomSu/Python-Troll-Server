# Python-Troll-Server
An API server designed for trolling the user who uses a pc with this installed. Written in python. This can be used remotely if you port forward port 80 in your router. You can ofcourse change the port to whatever you like.

# Installation
1. Have python3 installed
2. clone the repo
3. pip install -r requirements.txt
4. python shutdown.py

# Demo
[![Demo video](https://img.youtube.com/vi/AkmKBbu-gts/0.jpg)](https://www.youtube.com/watch?v=AkmKBbu-gts)

# Features
1. shutdown
2. restart
3. grab screenshot
4. show fake pop ups
5. control mouse
6. control keyboard, alt f4 and the best stuff
7. TTS, Text To Speach. I am using google variant gTTS

# routes
`/` [GET] (test if server is up)<br />
`/shutdown` [GET] (shuts down the pc)<br />
`/restart` [GET] (restarts the pc)<br />
`/alt_f4` [GET] (presses alt f4)<br />
`/move_mouse` [GET] (moves mouse to corner)<br />
`/mouse_spaz` [GET] (moves mouse in a square around the screen)<br />
`/showerror_spam` [GET] (creates multiple fake pop ups)<br />
`/screenshot` [GET] (takes a screenshot and sends the image)<br />

`/showerror` [POST]{`title`}{`message`} (create fake popup with title and message)<br />
`/text` [POST]{`text`}{`use_enter`} (type text on screen and press enter if use_enter is true)<br />
`/speak` [POST]{`text`}{`language`}{`slow`} (speak the text using language as dialect and speak slower if slow is true)<br />
