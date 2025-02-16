# Venv python

Venv python is a small utility to create python and pip executable along with a virtualenv they used. This is meant to to be used with command line scripts.

# Motivation
Creating command-line tools is a fairly common act when programming. In Python, the "accepted" way of doing this is to create a Python project with setuptools and add entrypoints which create executables that can be used from the command line and then install it with [pipx](https://github.com/pypa/pipx). However, this can be a hassle for small or numerous scripts. An alternative way of doing things, is to have Python scripts on your $PATH variables, with one big shared Python environment.

This all worked pretty well until new versions of Ubuntu started [preventing you from installing Python packages](https://www.reddit.com/r/learnpython/comments/1338la7/you_cant_use_pip_on_ubuntu_2304_anymore/) with pip. The approaches of having "one big shared virtualenv" used by the system and user tools was probably a bad one - but it often worked quite well.

I'm not going to give up using scripts on the my path, so I need a work around. One approach would to be to have my own version of Python that I use with all scripts. However, this felt a bit too wrong. So instead I have a shared version of Python used by each directory on my path.

This utility is defined to used to create these separate Python's.

# Installation

Use pipx to install venv-python (in it's own virtualenv)

```
pipx install venv-python
```

# Usage
If you have a directory on your path which contains python scripts. You can add a Python to it by cd'ing to it and running

```
venv-python $PREFIX
```

This will then create python called $PREFIX-python and a pip called $PREFIX-pip.

Then in your python scripts set the hashbang to:

```
#!/usr/bin/env $PREFIX-python

```

To install the dependencies of these scripts you can use $PREFIX-pip

# Alternatives and prior works
  * [ ] This is obviously just glue code about python virtualenvs. Pipx maintains a virtualenv for a project. You could instead use a single shared Python for all your scripts.

# About me
I am @readwithai. I write and make tools to do with [reading](https://readwithai.substack.com/p/what-is-reading-broadly-defined), productivity often using [Obsidian](https://readwithai.substack.com/p/what-exactly-is-obsidian)

If you are interested in this tool your might also be interested in:

1. This blog post about [sending code to a virtualenv](https://readwithai.substack.com/p/sending-code-to-a-python-virtualenv) from within Emacs using Ipython; or
2. This command-line tool to use [numpy from the shell](https://github.com/talwrii/npcli/blob/master/README.md)
3. This [library](command) that customizes pdb to be more useable by adding custom commands.

You can follow me on [X](https://x.com/readwithai) or my [blog](https://readwithai.substack.com)
