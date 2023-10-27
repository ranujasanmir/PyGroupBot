from setuptools import setup
import sys, os.path, shutil



if sys.version_info.major < 3:
    sys.stderr.write("pysimpqr requires Python 3.2+ ")
    sys.exit(1)

setup(name='PygroupBot',
      packages=['pygroupbot'],
      version="1.2.2",
      description='pygroupbot is python library that can you help to create your own simple telegram group manage bot',
      author='PixCap TM',
      url='https://github.com/ranujasanmir/pygroupbot',
      keywords=['telegram', 'bot'],
      license='BSD',
      classifiers = [
        'Environment :: Console',
        'Intended Audience :: Telegram Bot Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.5',
        ],
      install_requires = "pytelegrambotapi"
      long_description = open("README.md").read()
)

