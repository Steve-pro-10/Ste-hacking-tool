import ddos
art = r"""



"""

cm_list = """
DoS attack [1]

"""
class Tool():
    def __init__(self):
        pass
    def run(self):
        console = input("write the number of the tool $ ")
        console = console.split()
        comm = console[0]
        if int(comm) == 1: 
            nping,target = console[1] , console[2]
            ddos.Attack(nping,target).ping()

if __name__ == "__main__":
    app = Tool()
    while True:
        app.run()