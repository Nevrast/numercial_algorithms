import sys
from setuptools import setup, find_packages

src_folder = "."
sys.path.insert(0, src_folder)


setup(name='Distutils',
      version='1.0',
      description='Python Distribution Utilities',
      author='Greg Ward',
      author_email='gward@python.net',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=find_packages(src_folder))
