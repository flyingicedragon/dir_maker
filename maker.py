#!/usr/bin/env python
import argparse
import os
import subprocess

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

def make_dir(name, permission, group):
    os.mkdir(name)
    subprocess.run(['chmod', permission, name])
    subprocess.run(['chgrp', group, name])

def make_file(name, permission, group):
    new_file = open(name, mode='w')
    new_file.close()
    subprocess.run(['chmod', permission, name])
    subprocess.run(['chgrp', group, name])
