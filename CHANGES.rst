Changes
=======

2.0 (2018-02-22)
----------------

* The tests indicate `importchecker` still works for Python 2, but since
  the AST structures can differ between Python 2 and Python 3, no support is
  formally claimed.

1.2 (2018-02-21)
----------------

* Start on test coverage.

* Claim support for Python 2.7, drop claims for earlier versions.

1.1 (2012-01-09)
----------------

* Applied provided by wosc enabling running the import checker on
  individual python modules not just directories.

* Report the absolute path for modules when needed, relative paths (relative
  to the current working directory, that is) when possible.

1.0 (2008-05-06)
----------------

* Initial packaging

* Make the importchecker work on python 2.5
