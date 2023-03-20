from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.4.3'
DESCRIPTION = 'A simple but powerful GUI python package for overlays. Forked from EthanEdits/overlayGUI'
LONG_DESCRIPTION = 'A python package that uses Pygame to add an overlay to Windows'

# Setting up
setup(
    name="oGUI",
    version=VERSION,
    author="BoomBoomMushroom (Dillion Weaver)",
    author_email="<dillioncat7@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pygame', 'pywin32'],
    keywords=['python', 'overlay', 'pygame', 'powerful', 'easy', 'quick'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)
