import os

from setuptools import setup, find_packages


version = '1.2dev'


description = "Importchecker finds unused imports in Python modules."


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
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Natural Language :: English',
        'Operating System :: OS Independent',
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
    entry_points={
        'console_scripts': ['importchecker=importchecker.importchecker:main'],
        },
    )
