# -*- coding: utf-8 -*-

from setuptools import setup


def get_version_from_file():
    # get version number from __init__ file
    # before module is installed

    fname = 'sphinx_pdj_theme/__init__.py'
    with open(fname) as f:
        fcontent = f.readlines()
    version_line = [l for l in fcontent if 'VERSION' in l][0]
    return version_line.split('=')[1].strip().strip("'").strip('"')


def get_long_description_from_file():
    # content of README will be the long description

    fname = 'README.rst'
    with open(fname) as f:
        fcontent = f.read()
    return fcontent


VERSION = get_version_from_file()

DESCRIPTION = """
Dark sphinx theme based on the RTD theme.
""".strip()

LONG_DESCRIPTION = get_long_description_from_file()


setup(
    name='sphinx_pdj_theme',
    version=VERSION,
    url='https://github.com/jucacrispim/sphinx_pdj_theme',
    license='MIT',
    author='Juca Crispim',
    author_email='juca@poraodojuca.net',
    description='PdJ for Sphinx',
    long_description=LONG_DESCRIPTION,
    packages=['sphinx_pdj_theme'],
    include_package_data=True,
    entry_points={
        'sphinx.html_themes': [
            'sphinx_pdj_theme = sphinx_pdj_theme',
        ]
    },
    classifiers=[
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Theme',
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
