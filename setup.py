"""
Barman
--------

Barman helps you with your Flask
"""
from setuptools import setup


setup(
    name='Barman',
    version='0.0.1',
    url='',
    license='BSD',
    author='Mek Karpeles',
    author_email='michael.karpeles@gmail.com',
    description='A Flask application creator',
    long_description=__doc__,
    packages=[
        'barman'
        ],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'Flask-Routing'
    ],
    scripts=[
        "scripts/barman"
        ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
