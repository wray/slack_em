import time

from setuptools import find_packages

from distutils.core import setup

patch_level = int(time.time())

ver = "0.1." + str(patch_level)[4:]

setup(
  name = 'slackbot_ts',
  packages = find_packages(),
  version = ver,
  description = 'Python Code for Tech Em Studios Classes',
  author = 'Tech Em Studios',
  author_email = 'wray@techemstudios.com',
  url = 'https://github.com/wray/',
  download_url = 'https://github.com/wray//tarball/'+ver,
  keywords = ['slackbot', 'RPi', 'AWS'],
  classifiers = [],
)
