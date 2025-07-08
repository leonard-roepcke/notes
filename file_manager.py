import os
import shutil
class File_manager():
    def __init__(self):
        self.path = "notes/"

    def create_note(self):
        name = input("note name #")
        write_path = self.path+name+".txt"
        if os.path.exists(write_path) == False:
            text = input("write notes:")
            with open(write_path, "w") as f:
                f.write(text)
        else:
            print("This file exists already")
    
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
        self.path = os.path.dirname(self.path)
        self.path = os.path.dirname(self.path)
        self.path += "/"

    def schow_dir(self):
        print(self.path)

    def show_file(self):
        name = input("name: #")
        write_path = self.path+name+".txt"
        if os.path.exists(write_path):
            print("Inhalt von"+name+".txt:" +open(write_path, "r").read())
        else:
            print("This file doesen`t exit")
    
    def mk_dir(self):
        name = input("name #")
        os.mkdir(self.path+name)

    def del_file(self):
        name = input("name #")
        try: 
            if name.endswith(".txt"):
                os.remove(self.path+name)
            else:
                os.remove(self.path+name+".txt")
        except:
            print("no such file (use rm -rf to delet the dir)")

    def del_dir(self):
        name = input("name: #")
        shutil.rmtree(self.path+name)

    def edit_file(self):
        name = input("name: #")
        write_path = self.path+name+".txt"
        if os.path.exists(write_path):
            print(open(write_path, "r").read())
            text = input("write notes:")
            with open(write_path, "w") as f:
                f.write(text)
        else:
            print("This file doesen`t exit")
