from setuptools import setup, find_packages
import sys, os

version = '1.1'
description = "Importchecker finds unused imports in Python modules."

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('CHANGES.txt')
    + '\n' +
    read('CREDITS.txt')
    + '\n' +
    'Download\n'
    '========\n'
    )

setup(
    name='importchecker',
    version=version,
    description=description,
    long_description=long_description ,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Utilities',
        ],
    keywords='',
    author='Jan-Wijbrand Kolman',
    author_email='jw@n--tree.net',
    url='http://pypi.python.org/pypi/importchecker',
    license='ZPL 2.1',
    package_dir= {'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        ],
    entry_points={
        'console_scripts': ['importchecker=importchecker.importchecker:main'],
        },
    )
