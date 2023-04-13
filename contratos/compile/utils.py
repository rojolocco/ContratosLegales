# Imports
import os


# Delete latex compile files
def delete_compile_files(path, f):
    print(path)
    print(f)
    folder = os.listdir(path)
    print(folder)
    for item in folder:
        if item.startswith(f[-4:]):
            os.remove(os.path.join(path, item))
