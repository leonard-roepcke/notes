import file_manager
file_mg = file_manager.File_manager()

def fallback():
    print("wrong input")


map = {
    "ls": file_mg.show_files,
    "qn": file_mg.create_note,
    "cd": file_mg.move_in_dir,
    "pwd": file_mg.schow_dir,
    "mkdir": file_mg.mk_dir,
    "rm": file_mg.del_file,
    "rmdir": file_mg.del_dir,
    "edit": file_mg.edit_file,
    "cat": file_mg.show_file,
}

def input_handler():
    inp = input(file_mg.path+" #")
    teile = inp.strip().split(maxsplit=1)  # Zerlege in Befehl + Rest

    cmd = teile[0]  # z. B. "cd"
    arg = teile[1] if len(teile) > 1 else None

    func = map.get(cmd, fallback)

    if arg:
        func(arg)   # Mit Argument aufrufen
    else:
        func()      # Ohne Argument
    
