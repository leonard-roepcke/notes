import os
import shutil
class File_manager():
    def __init__(self, ref_ui_manager=""):
        self.path = "notes/"
        self.ref_ui_manager = ref_ui_manager

    def create_note(self, name=""):
        if name == "":
            print("No name was given")
            return

        write_path = self.path+name+".txt"
        if os.path.exists(write_path) == False:
            text = input("write notes:")
            with open(write_path, "w") as f:
                f.write(text)
        else:
            print("This file exists already")
    
    def show_files(self, dir=""):
        dateien = os.listdir(self.path+dir)
        for datei in dateien:
            print(datei)
        return(dateien)

    def move_in_dir(self, folder=""):
        new_dir = folder
        if folder == "..":
            self.cd_back()
            return
        if folder == "":
            print("no folder selected")
        dateien = os.listdir(self.path)
        for datei in dateien:
            if datei == new_dir:
                self.path += new_dir + "/"
                return
        print("path not found")

    def cd_back(self, name=""):
        self.path = os.path.dirname(self.path)
        self.path = os.path.dirname(self.path)
        self.path += "/"

    def schow_dir(self):
        print(self.path)

    def read_dir(self):
        return self.path

    def show_file(self, name=""):
        if name == "":
            print("no name was given")
            return
        write_path = self.path+name+".txt"
        if os.path.exists(write_path):
            print("Inhalt von"+name+".txt:" +open(write_path, "r").read())
        else:
            print("This file doesen`t exit")
    
    def mk_dir(self, name=""):
        if name == "":
            print("no name was given")
            return
        os.mkdir(self.path+name)

    def del_file(self, name=""):
        if name == "-rf":
            self.del_dir()
            return
        try: 
            if name.endswith(".txt"):
                os.remove(self.path+name)
            else:
                os.remove(self.path+name+".txt")
        except:
            print("no such file (use rm -rf to delet the dir)")

    def del_dir(self, name=""):
        if name == "":
            print("no name was given")
            return
        shutil.rmtree(self.path+name)

    def edit_file(self, name=""):
        if name == "":
            print("no name was given")
            return
        write_path = self.path+name+".txt"
        if os.path.exists(write_path):
            print(open(write_path, "r").read())
            text = input("write notes:")
            with open(write_path, "w") as f:
                f.write(text)
        else:
            print("This file doesen`t exit")
