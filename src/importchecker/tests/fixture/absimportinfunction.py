def foo():
    import sys
    import sys.stderr  # noqa: F401 imported but unused


class Bar(object):

    def __init__(self):
        import datetime
        import datetime.datetime  # noqa: F401 imported but unused
