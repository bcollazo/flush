from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='flush',
    version='1.0',
    description='Archive PostgreSQL tables to S3',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://github.com/bcollazo/flush',
    author='Bryan Collazo',
    author_email='bcollazo2010@gmail.com',
    license='MIT',
    packages=['flush'],
    install_requires=[
        'boto3',
        'psycopg2',
    ],
    entry_points={
        'console_scripts': ['flush=flush.main:main'],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
    ],
    zip_safe=False)
