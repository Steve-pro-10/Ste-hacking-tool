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
            
  
            # Usiamo Popen per esecuzione in tempo reale
            process = subprocess.Popen(
                [command],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,   
                shell=True,           # Output come stringhe, non bytes
                bufsize=1,              # Line buffered
                universal_newlines=True
            )

            # Leggiamo e stampiamo stdout in tempo reale
            for line in process.stdout:
                print(line, end='')  # end='' perché la riga ha già \n

            # Leggiamo eventuali errori (anche questi in tempo reale)
            for line in process.stderr:
                print(line, end='')

            # Aspettiamo che il processo termini per ottenere il codice di ritorno
            process.wait()



                
        except subprocess.TimeoutExpired:print("⏰ Timeout: il ping ha impiegato troppo tempo.")
        except Exception as e:print(f"Errore imprevisto: {e}")
