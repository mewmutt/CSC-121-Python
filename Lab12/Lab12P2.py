# Myles Joubert
# 4/11/23

import os


def show_files_and_dirs():
    print("Files and directories in current directory:")
    for item in os.listdir():
        print(item)


def main():
    show_files_and_dirs()

    if os.path.isfile('info.txt'):
        os.rename('info.txt', 'information.txt')
    else:
        print("File info.txt does not exist. Cannot rename.")

    if os.path.exists('information'):
        print("Directory information already exists. Cannot create.")
    else:
        os.mkdir('information')

    show_files_and_dirs()

if __name__ == '__main__':
    main()