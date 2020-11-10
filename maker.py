#!/usr/bin/env python
import argparse
import os
import subprocess
import sys

parser = argparse.ArgumentParser(description='make a new dir and change owner and/or permission.')
parser.add_argument(
    '-g',
    '--group',
    type=str,
    help='Group owner of dir.'
)
parser.add_argument(
    'name',
    type=str,
    help='Name of dir.'
)

def check_name(name):
    if name in os.listdir():
        print('error:', name, 'exists!', file = sys.stderr)
        sys.exit()

def make_dir(name, permission, group):
    check_name(name)
    os.mkdir(name)
    subprocess.run(['chmod', permission, name])
    if group:
        subprocess.run(['chgrp', group, name])

def make_file(name, permission, group):
    check_name(name)
    subprocess.run(['touch', name])
    subprocess.run(['chmod', permission, name])
    if group:
        subprocess.run(['chgrp', group, name])
