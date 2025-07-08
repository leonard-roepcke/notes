import file_manager
file_mg = file_manager.File_manager()

def fallback():
    print("wrong input")


map = {
    "ls": file_mg.show_files,
    "qn": file_mg.create_note,
    "rm -rf ." : file_mg.rm_all,
    "cd .." : file_mg.cd_back,
    "cd": file_mg.move_in_dir,
    "pwd": file_mg.schow_dir,
    "mkdir": file_mg.mk_dir,
    "rm": file_mg.del_file,
    "rm -rf": file_mg.del_dir,
    "rm -d": file_mg.del_dir,
    "rmdir": file_mg.del_dir,
    "edit": file_mg.edit_file,
    "cat": file_mg.show_file,
}

def input_handler():
    inp = input(file_mg.path+" #")
    map.get(inp, fallback)()
    
