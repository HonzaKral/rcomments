from os.path import join, dirname
from setuptools import setup


VERSION = (0, 0, 1)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

f = join(dirname(__file__), 'README.rst').open()
long_description = f.read().strip()
f.close()

install_requires = [
    'Django',
]
test_requires = [
    'nose',
    'coverage',
]

setup(
    name = 'APP_NAME',
    description = "APP_NAME",
    url = "https://github.com/WhiskeyMedia/APP_NAME/",
    long_description = long_description,
    version = __versionstr__,
    author = "Whiskey Media",
    author_email = "monitoring@whiskeymedia.com",
    packages = ['APP_NAME'],
    zip_safe = False,
    include_package_data = True,
    classifiers = [
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
    ],
    install_requires=install_requires,

    test_suite='test_APP_NAME.run_tests.run_all',
    test_requires=test_requires,
)
