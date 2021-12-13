from setuptools import setup, find_packages

setup(
    name='PyQtPlus',
    version='0.0.1',
    packages=find_packages(include=['PyQtPlus', 'PyQtPlus.*']),
    install_requires=['PyQt6']
)