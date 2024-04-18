# Created on April 17 2024
# Description: A simple file and directory scanner written in Python
# Version: 1.0
# Python version: 3.12.1
# License: GNU
# @author: andrew thomas

from encodings import utf_8
import os, random

# For the given path, get the List of all files in the directory tree 

def get_list_of_files(dir_name):
    # create a list of file and subdirectories
    list_of_file = os.listdir(dir_name)
    all_files = []

    # Iterate over all the entries
    for entry in list_of_file:
        # Create full path
        full_path = os.path.join(dir_name, entry)
        # If entry is a directory then get the list of files in this directory
        try:
            if os.path.isdir(full_path):
                all_files.extend(get_list_of_files(full_path))
                colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']
                for letter in "+-- Scanning --+":
                    color = random.choice(colors)
                    print(f"{color}{letter}", end='')
                print('\033[0m', end='\r')
            else:
                all_files.append(full_path)
        except PermissionError:
            print("\033[95mAccess to the directory was denied:\033[0m", full_path,)
            all_files.append("ACCESS DENIED to " + full_path)

    return all_files if all_files else []  # Return an empty list if no files found

def main():
    # clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    # display prompt and ask for the file path to be scanned
    print('''
 ▄▄▄· ▄· ▄▌.▄▄ ·  ▄▄· ▄▄▄   ▄▄▄·  ▄▄▄·▄▄▄ .
▐█ ▄█▐█▪██▌▐█ ▀. ▐█ ▌▪▀▄ █·▐█ ▀█ ▐█ ▄█▀▄.▀·
 ██▀·▐█▌▐█▪▄▀▀▀█▄██ ▄▄▐▀▀▄ ▄█▀▀█  ██▀·▐▀▀▪▄
▐█▪·• ▐█▀·.▐█▄▪▐█▐███▌▐█•█▌▐█▪ ▐▌▐█▪·•▐█▄▄▌
.▀     ▀ •  ▀▀▀▀ ·▀▀▀ .▀  ▀ ▀  ▀ .▀    ▀▀▀ 
''')
    print(43 * "-")
    print("|-- pyscrape file and directory scanner --|")
    print("|             -- Version 1.0 --           |")
    print("|    -- by Andrew Thomas (asteng88) --    |")
    print("|--  Scans local and network locations  --|")
    print(43 * "-")
    print("\n")
    file_path = input("Specify the Drive or File path: ")
    dir_name = file_path
    counting = 0
    # get the list of all files in directory tree at given path
    complete_list = get_list_of_files(dir_name)
    # add the files to an empty text file called "pyscrape_out.txt" and "pyscrape_out.html"
    with open("pyscrape_out.txt", "w", encoding='utf_8') as txt_file, open("pyscrape_out.html", "w", encoding='utf_8') as html_file:
        txt_file.write("List of Files:\n")
        html_file.write("<html>\n<head>\n<title>List of Files</title>\n</head>\n<body>\n")
        for elem in complete_list:
            txt_file.write(elem)
            txt_file.write("\n")
            html_file.write(f"<a href='{elem}'>{elem}</a><br>\n")
            counting += 1
        html_file.write("</body>\n</html>")
    print("\nCompleted.", counting, "files found.")
    print("Files saved as 'pyscrape_out.txt' and 'pyscrape_out.html' in the current directory.")
    run_again = input("Would you like to run again? (y/n): ")
    if run_again.lower() == "y":
        main()
    else:
        print("Goodbye.")
        exit()

if __name__ == '__main__':
    main()
