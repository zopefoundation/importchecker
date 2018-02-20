import io
import unittest
import pkg_resources

from importchecker.importchecker import main


class TestImportChecker(unittest.TestCase):

    def test_abs_import(self):
        source = pkg_resources.resource_filename(
            'importchecker.tests', 'fixture/absimport.py')
        output = io.StringIO()
        main(path=source, stdout=output)
        self.assertEqual(
            'src/importchecker/tests/fixture/absimport.py:1: sys\n'
            'src/importchecker/tests/fixture/absimport.py:2: sys.stderr\n',
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
