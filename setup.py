from setuptools import setup
import re
required_packages =[
    'Django==3.1.7',
]

VERSION_RE = re.compile(r'__version__ = \'([\d\.]+)\'')


def read_version():
    with open('djangopnp/__init__.py') as file:
        version_line = [line for line in file.readlines()
                        if line.startswith('__version__')][0]
        return VERSION_RE.match(version_line).groups()[0]

setup(
   name='django pnp',
   version=read_version(),
   description='An application to display pnp machine status',
   author='Daniel Harrington',
   author_email='djangpnp@rotair.com',
   packages=['djangopnp'],  #same as name
   install_requires=required_packages, #external packages as dependencies
   classifiers=[
        'Topic :: Internet',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    package_data={
    },
    zip_safe=False

)
