from distutils.core import setup
setup(
  name = 'sticks',
  packages = ['sticks'], # this must be the same as the name above
  version = '0.13',
  description = 'A random test lib',
  author = 'ganesh',
  author_email = 'ganeshhubale@gmail.com',
  url = 'https://github.com/ganeshhubale/game_of_sticks', 
 # download_url = 'https://github.com/peterldowns/mypackage/archive/0.1.tar.gz', # I'll explain this in a second
  keywords = ['testing', 'logging', 'sticks'], # arbitrary keywords
  classifiers = [],
     entry_points={
         'console_scripts': [
             'sticks = sticks.__init__:main',
],
         },
)

