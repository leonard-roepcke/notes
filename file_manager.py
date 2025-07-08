import os
class File_manager():
    def __init__(self):
        self.path = "notes/"

    def create_note(self):
        name = input("note name #")
        text = input("write notes:")
        with open(self.path+name+".txt", "w") as f:
            f.write(text)
    
    def show_files(self):
        dateien = os.listdir(self.path)
        for datei in dateien:
            print(datei)

    def rm_all(self):
        print("rm files not implementet jet")

    def move_in_dir(self):
        new_dir = input("dir: #")
        dateien = os.listdir(self.path)
        for datei in dateien:
            if datei == new_dir:
                self.path += new_dir + "/"
                return
        print("path not found")

    def cd_back(self):
        print("cd back not implementet jet")
        