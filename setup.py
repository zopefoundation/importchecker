import os
import sys

from setuptools import setup, find_packages


version = '2.0+md.2.dev0'


description = "Importchecker finds unused imports in Python modules."
test_requirements = ['zope.testrunner']

if sys.version_info.major == 2:
    test_requirements.append('mock')


def read(*rnames):
    filename = os.path.join(os.path.dirname(__file__), *rnames)
    with open(filename, 'r') as txt:
        return txt.read()


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
    long_description=long_description,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        ],
    keywords='',
    author='Jan-Wijbrand Kolman',
    author_email='jw@n--tree.net',
    url='http://pypi.python.org/pypi/importchecker',
    license='ZPL 2.1',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
    tests_require=test_requirements,
    extras_require={'test': test_requirements},
    entry_points={
        'console_scripts': ['importchecker=importchecker.importchecker:main'],
        },
    )
