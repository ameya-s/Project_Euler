#! python
import sys
import os
from os import listdir
from os.path import isfile, join

pythonScripts = [f for f in os.listdir('./') if isfile(join('./', f)) and '.py' in f]

batchScript = '@echo off\nsetlocal ENABLEDELAYEDEXPANSION\nSET full_file_path=%~f0\nSET full_file_path=!full_file_path:bat=py!\nECHO !full_file_path!\n@echo on\n@py.exe !full_file_path! %*\n@echo off\nENDLOCAL\nPAUSE'
for script in pythonScripts:
    batchFileName = script.replace('.py','.bat')
    batch = open( batchFileName , 'w')
    batch.write(batchScript)
    batch.close
