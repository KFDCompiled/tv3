from setuptools import setup

setup(
    name='terminal_velocity',
    version='0.1.10',
    author='Sean Hammond, Vincent Perricone, Aramís Concepción Durán',
    packages=['terminal_velocity'],
    scripts=['bin/terminal_velocity'],
    url='github.com/aramiscd/terminal_velocity',
    license='GNU General Public License, Version 3',
    description='A fast note-taking app for the UNIX terminal',
    long_description=open('README.md').read(),
    install_requires=[
        'urwid==1.1.1',
        'chardet==2.1.1',
        ],
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2 :: Only',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        ],
)
