#!/bin/bash/python3
import subprocess
import glob
import platform
import install_ffmpeg_verify


def choice_file():
    print("Choice 1 for [.mp4] or 2 for exit.")
    file_type = input("What is the file type ?\n")
    
    if int(file_type) == 1:
        read_directory(file_type)
    else:
        stop()


def read_directory(file_type):
    
    if int(file_type) == 1:
        file_type = 'mp4'
    
    target_file = glob.glob("*." + file_type)
    print("Search file ." + file_type)
    print('#####################')

    if len(target_file) > 0:
        files_found(target_file)
    else:
        print('Files not found.')
        print('#####################')
        stop()

   
def files_found(target_file):
    print('files found:')
    for files in target_file:
        print('=> ' + files)
        
        new_format = files.replace('.mp4', '.mp3')
        
        exec_extraction(files, new_format)


def exec_extraction(old_format, new_format):
    subprocess.run(
        'ffmpeg -i '+old_format+' finalized/'+new_format, shell=True
    )
    
    msg = 'Converting: '+old_format+ ' => '+new_format
    print('------------------------------------------>')
    print(msg)
    print('------------------------------------------>')
    print('Finished!')


def clear_directory():
    print('Clear file text...')
    subprocess.run(
        'echo "Clear..." > ffmpeg-version.txt', shell=True
    )  


def stop():
    print('Stopping execution.')
    print('#####################')
    exit()


def run():
    print("Starting script...")
    print('#####################')
    
    install_ffmpeg_verify.ffmpeg_is_installed()
    clear_directory()
    choice_file()


if __name__ == '__main__':
    run()