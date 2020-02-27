import subprocess
import re


def ffmpeg_is_installed():
    print('Verify if ffmpeg is installed!')
    print('===============================>')
    subprocess.run(
        'ffmpeg -version 2>&1 > ffmpeg-version.txt', shell=True
    )
    
    file = open('ffmpeg-version.txt', 'r')
    
    content_file = file.read()
    
    file.close()
    
    regex = re.compile(r'ffmpeg version \d+.\d+.\d+')
    if regex.match(content_file):
        print('--------------------->')
        print('ffmpeg is installed, continue!')
        print('--------------------->')
        print(content_file)
    else:
        print('ffmpeg not is installed!')
        print('===============================>')
        verify_os()


def verify_os():
    os_type = platform.system()
    
    if os_type == 'Darwin':
        install_ffmpeg_mac()
    elif os_type == 'Linux':
        install_ffmpeg_linux()


def install_ffmpeg_mac():
    print('Installing ffmpeg at mac os!')
    print('===============================>')
    subprocess.run(
        'brew install ffmpeg', shell=True
    )


def install_ffmpeg_linux():
    print('Installing ffmpeg at linux!')
    print('===============================>')
    subprocess.run(
        'sudo apt-get install ffmpeg', shell=True
    )

