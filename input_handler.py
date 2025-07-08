import file_manager
file_mg = file_manager.File_manager()



def fallback():
    print("wrong input")



map = {
    "ls": file_mg.show_files,
    "qn": file_mg.create_note,
    "rm -rf ." : file_mg.rm_all,
}

def input_handler():
    inp = input("#")
    map.get(inp, fallback)()
    
