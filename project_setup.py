#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import shutil

import reusables

here = os.path.abspath(os.path.dirname(__file__))


def c(path):
    return os.path.abspath(os.path.join(here, path))


print('WARNING: This will rename and modify all these projects files in place,'
      ' do not use if project has already been set up!\n\n')

program_name = input('What do you want us to call your program? :').strip()

shutil.copytree(c('project_name'), c(program_name))
shutil.rmtree(c('project_name'))
shutil.move(c('project_name.logging.yaml'), c(f'{program_name}.logging.yaml'))
shutil.move(c('project_name.nginx'), c(f'{program_name}.nginx'))
shutil.move(c('project_name.service'), c(f'{program_name}.service'))
shutil.move(c(os.path.join(program_name, 'static', 'css', 'project_name.css')),
            c(os.path.join(program_name, 'static', 'css', f'{program_name}.css')))
shutil.move(c(os.path.join(program_name, 'static', 'js', 'project_name.js')),
            c(os.path.join(program_name, 'static', 'js', f'{program_name}.js')))


def replace_file(replace_file):
    global program_name
    with open(replace_file, 'r+') as f:
        data = f.read().replace('<project_name>',
                                program_name).replace('project_name',
                                                      program_name)
        f.seek(0)
        f.write(data)


for file in list(reusables.find_files(program_name,
                                      ext=('css', 'js', 'py', 'html'))):
    replace_file(file)


for file in [f'{program_name}.logging.yaml',
             f'{program_name}.nginx',
             f'{program_name}.service',
             '.gitignore',
             'README.md']:
    replace_file(file)

print('Setup has completed, you may now delete this file')


