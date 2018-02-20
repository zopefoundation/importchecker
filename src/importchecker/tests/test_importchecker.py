import io
import unittest
import pkg_resources

from importchecker.importchecker import main


class TestImportChecker(unittest.TestCase):

    def test_no_path_supplied(self):
        import sys

        output = io.StringIO()
        orig = sys.argv[:]
        sys.argv[:] = []
        with self.assertRaises(SystemExit):
            main(stdout=output)
        self.assertEqual(
            'No path supplied\n',
            output.getvalue())
        sys.argv[:] = orig

    def test_abs_import(self):
        source = pkg_resources.resource_filename(
            'importchecker.tests', 'fixture/absimport.py')
        output = io.StringIO()
        main(path=source, stdout=output)
        self.assertEqual(
            'src/importchecker/tests/fixture/absimport.py:1: sys\n'
            'src/importchecker/tests/fixture/absimport.py:2: sys.stderr\n',
            output.getvalue())

    def test_abs_import_in_function(self):
        source = pkg_resources.resource_filename(
            'importchecker.tests', 'fixture/absimportinfunction.py')
        output = io.StringIO()
        main(path=source, stdout=output)
        self.assertEqual(
            'src/importchecker/tests/fixture/absimportinfunction.py:2: sys\n'
            'src/importchecker/tests/fixture/absimportinfunction.py:3: sys.stderr\n'
            'src/importchecker/tests/fixture/absimportinfunction.py:9: datetime\n'
            'src/importchecker/tests/fixture/absimportinfunction.py:10: datetime.datetime\n',
            output.getvalue())

    def test_from_import(self):
        source = pkg_resources.resource_filename(
            'importchecker.tests', 'fixture/fromimport.py')
        output = io.StringIO()
        main(path=source, stdout=output)
        self.assertEqual(
            'src/importchecker/tests/fixture/fromimport.py:1: stderr\n',
            output.getvalue())

    def test_from_import_as(self):
        source = pkg_resources.resource_filename(
            'importchecker.tests', 'fixture/fromimportas.py')
        output = io.StringIO()
        main(path=source, stdout=output)
        self.assertEqual(
            'src/importchecker/tests/fixture/fromimportas.py:1: stderr\n',
            output.getvalue())

    def test_attr_assigment(self):
        """In the Python 2 `compiler`-based implementation there was a
        specific codepath for attribute assignment nodes.
        """
        source = pkg_resources.resource_filename(
            'importchecker.tests', 'fixture/attrassignment.py')
        output = io.StringIO()
        main(path=source, stdout=output)
        self.assertEqual(
            '',
            output.getvalue())

    def test_abs_import_attr_assigment(self):
        """This case was originally reported in the README to trigger a false
        positive. This seems no longer the case.
        """
        source = pkg_resources.resource_filename(
            'importchecker.tests', 'fixture/absimportattrassignment.py')
        output = io.StringIO()
        main(path=source, stdout=output)
        self.assertEqual(
            '',
            output.getvalue())

    def test_call_imported_name(self):
        """This case was originally reported in the README to trigger a false
        positive. This seems (no longer) the case.
        """
        source = pkg_resources.resource_filename(
            'importchecker.tests', 'fixture/callimportedname.py')
        output = io.StringIO()
        main(path=source, stdout=output)
        self.assertEqual(
            '',
            output.getvalue())


class TestImportCheckerOnDirectory(unittest.TestCase):

    def test_importchecker(self):
        source = pkg_resources.resource_filename(
            'importchecker.tests', 'fixture')
        output = io.StringIO()
        main(path=source, stdout=output)
        self.assertEqual(
            'src/importchecker/tests/fixture/absimport.py:1: sys\n'
            'src/importchecker/tests/fixture/absimport.py:2: sys.stderr\n'
            'src/importchecker/tests/fixture/absimportinfunction.py:2: sys\n'
            'src/importchecker/tests/fixture/absimportinfunction.py:3: sys.stderr\n'
            'src/importchecker/tests/fixture/absimportinfunction.py:9: datetime\n'
            'src/importchecker/tests/fixture/absimportinfunction.py:10: datetime.datetime\n'
            'src/importchecker/tests/fixture/fromimport.py:1: stderr\n'
            'src/importchecker/tests/fixture/fromimportas.py:1: stderr\n',
            output.getvalue())
