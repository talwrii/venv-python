
from setuptools import setup

setup(
    name='venv-python',
    version="1.0.1",
    author='readwithai',
    author_email='talwrii@gmail.com',
    description='Create a specially named python and pip for use with scripts',

    license='MIT',
    keywords='scripts, virtualenv',
    url='https://github.com/talwrii/venv_python',
    packages=["venv_python"],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    entry_points={
        'console_scripts': ['venv-python=venv_python.main:main']
    },
)
