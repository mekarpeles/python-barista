"""
Barista
-------

Barista helps you manage the Flask
"""

from distutils.core import setup

setup(
    name='Barista',
    version='0.0.22',
    url='',
    license='BSD',
    author='Mek Karpeles',
    author_email='michael.karpeles@gmail.com',
    description='A Flask application creator',
    long_description=__doc__,
    packages=[
        'barista'
        ],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'Flask-Routing'
    ],
    scripts=[
        "scripts/barista"
        ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
