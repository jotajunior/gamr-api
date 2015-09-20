from setuptools import setup, find_packages

setup(name = 'gamr',
        version = '0.1',
        install_requires = ['requests',
         'Flask',
         'Flask-Cache',
         'lxml',
         ],
        packages = find_packages(),
        package_dir = {'':'src'},
)
