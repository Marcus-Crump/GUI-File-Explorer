import os, sys, subprocess, platform
import assets.guiComponents as GUI
from PyQt5.QtWidgets import QApplication

def get_starting_path(system):
    if system == "Windows":
        return os.path.expanduser("%HOMEPATH%").strip()
    else:
        return os.path.expanduser("~/").strip()

def initialize():
    system = platform.system()
    start = get_starting_path(system)
    items = subprocess.check_output(["ls",start],text=True).strip().split()
    return system, start, items

def main():
    app = QApplication(sys.argv)
    op,path,items = initialize()
    window = GUI.MainWindow(op, path, items)
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()