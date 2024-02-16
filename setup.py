import os

from setuptools import find_packages
from setuptools import setup


version = '3.0'
description = "Importchecker finds unused imports in Python modules."
test_requirements = [
    'zope.testrunner'
]


def read(*rnames):
    filename = os.path.join(os.path.dirname(__file__), *rnames)
    with open(filename) as txt:
        return txt.read()


long_description = (
    read('README.rst')
    + '\n' +
    read('CHANGES.rst')
    + '\n' +
    read('CREDITS.rst')
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
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    keywords='',
    author='Jan-Wijbrand Kolman',
    author_email='zope-dev@zope.dev',
    url='https://github.com/zopefoundation/importchecker',
    license='ZPL 2.1',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.7',
    install_requires=['setuptools'],
    tests_require=test_requirements,
    extras_require={'test': test_requirements},
    entry_points={
        'console_scripts': ['importchecker=importchecker.importchecker:main'],
    },
)
