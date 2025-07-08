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
        self.path = os.path.dirname(self.path)
        self.path = os.path.dirname(self.path)
        self.path += "/"

    def schow_dir(self):
        print(self.path)
    
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
        os.rmdir(self.path+name)