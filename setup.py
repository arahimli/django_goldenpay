from setuptools import setup, find_packages
import setuptools
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Make Payments by GoldenPay'
LONG_DESCRIPTION = 'A package that makes goldenpay payment url'

# Setting up
setup(
    name="django_goldenpay",
    version=VERSION,
    author="Atakhan Rahimli",
    author_email="<ataxanr@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests', 'xmltodict', 'django'],
    keywords=['python', 'django', 'payment', 'goldenpay', 'goldenpay django', 'goldenpay python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)