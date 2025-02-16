# Create setup.py for pip for this directory

# llm command: find .
# llm file: venv_python/main.py


# This should add an executbale entry point called venv-python
# You should
# 1. Include the package (derive this from the result of find .)
# 2. Use entry_points
# 3. Add the following fields
#   - Author: readwithai
#   - Email: talwrii@gmail.com
#   - url: (note that I'm talwrii on github, add the project pagae accordingly)
# 4. Add scripts and virtualenv as keywords. (Keywords is a csv)


# Here is an example setup
# setuptools.setup(
#     name='',
#     version=0.1,
#     author='Author',
#     long_description_content_type='text/markdown',
#     author_email='Email',
#     description='',
#     license='GPLv3',
#     keywords='',
#     url='',
#     packages=[],
#     long_description=open('README.md').read(),
#     entry_points={
#         'console_scripts': ['=.:main']
#     },
# )

# Use an MIT license

# 1. Include the package (derive this from the result of find .)
# 2. Description: Create a specially named python and pip for use with scripts

from setuptools import setup

setup(
    name='venv_python',
    version=0.1,
    author='readwithai',
    author_email='talwrii@gmail.com',
    description='Create a specially named python and pip for use with scripts',
    license='MIT',
    keywords='scripts,virtualenv',
    url='https://github.com/talwrii/venv_python',
    packages=["venv_python"],
    long_description=open('README.md').read(),
    entry_points={
        'console_scripts': ['venv-python=venv_python.main:main']
    },
)
