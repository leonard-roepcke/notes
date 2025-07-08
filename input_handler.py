import file_manager
file_mg = file_manager.File_manager()

def show_files():
    print("files :)")

def fallback():
    print("wrong input")



map = {
    "ls": show_files,
    "qn": file_mg.create_note,
}

def input_handler():
    inp = input("#")
    map.get(inp, fallback)()
    
