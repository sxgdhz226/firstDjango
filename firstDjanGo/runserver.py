#!/usr/bin/env python
from multiprocessing import Process
import subprocess
import os
import configparser

BASEPATH = os.path.dirname(os.path.abspath(__file__))

def startdjango():
    os.chdir(os.path.join(BASEPATH, ''))
    # subprocess.call('python manage.py runserver 0.0.0.0:8000', shell=True)
    subprocess.call('python manage.py runserver 0.0.0.0:8000')


def main():
    django = Process(target=startdjango, args=())
    django.start()

    django.join()

if __name__ == "__main__":
    main()
