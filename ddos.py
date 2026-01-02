import subprocess
import platform
import sys


class Attack():
    def __init__(self, num_ping, target):
        self.num_ping = num_ping
        self.target = target
    def ping(self):
        """
        Pinga un sito web o indirizzo IP.
        
        Parametri:
        - host: il dominio o IP da pingare (es. "google.com")
        - count: numero di pacchetti da inviare
        """
        if int(self.num_ping) < 1: self.num_ping = 4
        

        system = platform.system()
        if system == "Windows": parameter = "-n"
        else: parameter = "-c"
        
        command = f"ping {parameter} {self.num_ping} {self.target}"
        try:
            
            out = subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
                
                # Stampa l'output completo del comando ping
            if out.stdout:
                print(out.stdout.decode('utf-8', errors='ignore'))  # invece di print(out.stdout)
            if out.stderr:
                print(out.stderr.decode('utf-8', errors='ignore'))

                
        except subprocess.TimeoutExpired:print("⏰ Timeout: il ping ha impiegato troppo tempo.")
        except Exception as e:print(f"Errore imprevisto: {e}")
