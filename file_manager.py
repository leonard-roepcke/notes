class File_manager():
    def __init__(self):
        self.path = "notes/"

    def create_note(self):
        name = input("note name #")
        text = input("write notes:")
        with open(self.path+name+".txt", "w") as f:
            f.write(text)