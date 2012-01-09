Importchecker
=============

What is importchecker?
----------------------

Importchecker is a commandline utility to find unused imports in Python
modules.

Its output is "grep-like" (and thus "emacs-friendly"), reporting both the
module's filenames and line numbers where names are imported that are not
acually used in the module.

Importchecker will not modify any of the source files. Whether the import
needs to be removed is left to the judgement of the developer.

Installation
------------

The importchecker commandline utility can be installed using the
``easy_install`` command::

  $ sudo easy_install importchecker

The command can then be invoked with either a directory or a Python file::

  $ importchecker /path/to/a/source/tree
  $ importchecker /path/to/a/source/tree/module.py

Buildout
--------

Projects that make use of `zc.buildout`_ for development might find the
following ``buildout.cfg.`` snippet useful for using the importchecker on
the developed codebase::

  [buildout]
  ...
  parts = importchecker ...
  ...

  [importchecker]
  recipe = zc.recipe.egg
  eggs = importchecker
  arguments = "${buildout:directory}/src"

.. _`zc.buildout`: http://pypi.python.org/pypi/zc.buildout

Known issues
------------

* One source tree path argument at the time can be passed to the command
  line utility.

* Command line argument parsing is rather naïve.
