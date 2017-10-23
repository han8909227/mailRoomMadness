from setuptools import setup

setup(
    name='mailroom',
    package_dir={'': 'src'},
    py_modules=['mailroom'],
    author='Fortunato Maycotte Han Bao Megan Flood',
    author_email='fortunato.maycotte@gmail.com',
    description='Emails to donors and organizes contributions',
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox', 'Faker']},
    entry_points={'console_scripts': ['mailroom = mailroom:main']}
)