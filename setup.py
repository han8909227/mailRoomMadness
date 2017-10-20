from setuptools import setup 

setup(
    name='mailroom',
    package_dir={'':'src'},
    py_modules=['mailroom'],
    author='Fortunato Maycotte Han Bao Megan Flood',
    author_email='fortunato.maycotte@gmail.com',
    description='Emails to doners and organizes contributions',
    install_requires=[],
    exrtras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']},
    entry_points={'console_scripts': []}
    )