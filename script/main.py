import os
import shutil

# List of some comman files
extDic = {
    "Audio Files": [".aif", "cda", "mid", "midi", "mp3", "mpa", "ogg", "wav", "wma", "wpl"],
    "Compressed Files": ["7z", "arj", "deb", "pkg", "rar", "rpm", "tar", "z", "zip"],
    "Documents": ["docx", "pdf", "pps", "ppt", "pptx", 'odt', 'xlsx', 'xlsm', 'txt', 'tex', 'rtf'],
    "Executable files": ['apk', 'bat', 'exe', 'gadget', 'jar', 'msi', 'wsf'],
    "Internet Files": ["asp", "aspx", "cer", "cfm", "css", "html", "htm"],
    "Images": ['ai', 'bmp', 'gif', 'ico', 'jpeg', 'jpg', 'png', 'svg', 'tif', "tiff"],
    "Programming files": ["c", "cgi", "pl", "class", "cpp", "cs", "h", "java", "js", "php", 'py', "sh", "swift", "vd"]
}


def renameFile(path, file, folder):
    """
    rename if the file is already in the folder
    """
    count = 1
    while os.path.exists(os.path.join(path, os.path.join(folder, file))):
        x = file.split(".")[0] + f'copy({count}).' + file.split(".")[-1]
        os.rename(os.path.join(path, file), os.path.join(path, x))
        file = x
    shutil.move(os.path.join(path, file), os.path.join(path, folder))


def checkAndMove(path, file, folder):
    """
        check if the folder exist,
        if not make it
    """
    if os.path.exists(os.path.join(path, folder)):
        renameFile(path, file, folder)
    else:
        os.mkdir(os.path.join(path, folder))
        renameFile(path, file, folder)


if __name__ == "__main__":
    try:
        PATH = input("Enter a Path or Darg the Folder Here: ")
        if not os.path.exists(PATH):
            raise Exception

        # list all the files and dir in path
        files = os.listdir(PATH)
        for file in files:
            if os.path.isfile(os.path.join(PATH, file)):
                ext = file.split(".")[-1].lower()
                for folder in extDic:
                    if ext in extDic[folder]:
                        checkAndMove(PATH, file, folder)

        # list all the files and dir left in path
        unknowFiles = os.listdir(PATH)
        for file in unknowFiles:
            if os.path.isfile(os.path.join(PATH, file)):
                checkAndMove(PATH, file, "Others")
        print("All files are Organized!")
    except:
        print("Some error Occured")
