from setuptools import setup, find_packages

setup(  
    name="sticks",
    packages=find_packages(),
    version='0.0.1',
    description="Simple game application.",
    long_description="long description.",
    author="ganeshhubale.",
    author_email="ganeshhubale03@gmail.com",
    url="https://github.com/ganeshhubale/game_of_sticks",
    license="MIT",
    py_modules=['sticks.__init__'],
    namespace_packages=[],
    entry_points={
        'console_scripts': [
            'sticks = sticks.__init__:main',
        ],
    },
)
