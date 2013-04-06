# coding: utf-8
import os
import re
import commands
from distutils.core import setup
from distutils.command.install import install


HOME_DIRECTORY = os.path.expanduser("~")
BASHRC_FILE = '.bashrc'
BASHRC_PATH = os.path.join(HOME_DIRECTORY, BASHRC_FILE)

RE = re.compile(r'^\. .*goto.sh')


def post_install():
    """
    Edits .bashrc file to source goto.sh script.
    """
    status, goto_sh_path = commands.getstatusoutput('which goto.sh')

    if status != 0:
        print 'Can\'t find goto.sh script.'
        return

    source_line = ". %s\n" % goto_sh_path

    with open(BASHRC_PATH, 'r') as f:
        lines = f.readlines()

    replaced = False

    with open(BASHRC_PATH, 'w') as f:
        for line in lines:
            if RE.match(line):
                replaced = True
                f.write(source_line)
            else:
                f.write(line)

        if not replaced:
            f.write('\n')
            f.write(source_line)


class GotoInstall(install):
    def run(self):
        install.run(self)
        post_install()


setup(
    name='goto-dir',
    version='0.1.0',
    author='Paulo Borges',
    author_email='pauloborgesfilho@gmail.com',
    packages=['goto','goto.test'],
    scripts=['bin/bootstrap_goto.py', 'bin/goto.sh'],
    url='http://pypi.python.org/pypi/goto-dir/',
    license='See LICENSE.',
    description='easy\'n\'fast cd\'ing.',
    long_description=open('README.md').read(),
    cmdclass={ 'install': GotoInstall },
)