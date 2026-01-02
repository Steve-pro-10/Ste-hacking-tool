import ddos
art = r"""



"""

cm_list = """
COMMAND LIST:
DoS attack [1] 

TYPE "[COMMAND NUMBER] help" to view the parameters of the command
"""
help = {

   1 : "DDOS ATTACK:\n Syntax: 1 [number of pings] [target (ip address of domain)]\n Es. 1 6 google.com" 
}

print(cm_list)
class Tool():
    def __init__(self):
        pass
    def run(self):
        console = input("write the number of the tool $ ")
        console = console.split()
        comm = console[0]
        #DDOS ATTACK
        if comm == "1" and console[1] == "help": print(help[1])
        else: 
            try:
                nping,target = console[1] , console[2]
                ddos.Attack(nping,target).ping()
            except IndexError: print("Error: Missing parameters")

if __name__ == "__main__":
    app = Tool()
    while True:
        app.run()