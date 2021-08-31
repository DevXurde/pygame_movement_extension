from setuptools import setup, find_packages
import codecs
import os

VERSION = "2.0.2"
DESCRIPTION = "This is a pygame extension to exhibit movement in a few lines for documentation visit https://github.com/ZayedMalick/pygame_movement_extension"

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3",
    "Operating System :: Unix",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: MacOS :: MacOS X",
    "License :: OSI Approved :: MIT License"
]

# Setting Up
setup(
    name="pygame_movement",
    version=VERSION,
    author="DevXurde (Zayed Malick)",
    author_email="thexurde123@gmail.com",
    description=DESCRIPTION,
    long_description=open('README.md').read() + '\n\n' +
    open('CHANGELOG.txt').read(),
    packages=find_packages(),
    install_requires=["pygame", "rich"],
    keywords=["python", "pygame", "rich-text", "extension",
              "games", "movement", "game-development"],
    classifiers=classifiers,
    url="https://github.com/ZayedMalick/pygame_movement_extension",
    license="MIT"
)
