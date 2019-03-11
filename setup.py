from setuptools import setup

setup(
    name='flush',
    version='0.1',
    description='Archive PostgreSQL tables to S3',
    url='http://github.com/bcollazo/flush',
    author='Bryan Collazo',
    author_email='bcollazo2010@gmail.com',
    license='MIT',
    packages=['flush'],
    install_requires=[
        'boto3',
    ],
    entry_points={
        'console_scripts': ['flush=flush.main:main'],
    },
    zip_safe=False)
