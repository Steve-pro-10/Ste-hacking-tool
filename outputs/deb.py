import socket

class Main:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def run(self):
        self.s.bind(("0.0.0.0", 8080))
        self.s.listen(5)
        print("Server is searching for clients...")

        while True:    
            conn, victim_addr = self.s.accept()
            print(f"\nVictim connected: {victim_addr}")

            while True:
                try:
                    dati = conn.recv(2048)
                    if not dati:
                        print(f"{victim_addr} closed the connection.")
                        break
                    testo = dati.decode("utf-8").strip()
                    if testo:  # evita linee vuote
                        print(f"Recieved: {testo}")
                except ConnectionResetError:
                    print(f"Connection restarted {victim_addr}")
                    break

            conn.close()
            print(f"Connection with {victim_addr} closed.\n")

if __name__ == "__main__":
    app = Main()
    try:
        app.run()
    except KeyboardInterrupt:
        print("\nServer terminato.")
    finally:
        app.s.close()