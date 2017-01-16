from setuptools import setup, find_packages
from codecs import open
from os import path

__version__ = 'v0.0.1'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')]

setup(
    name='opac_ssm_api',
    version=__version__,
    description='gRPC API of OPAC-SSM service',
    long_description=long_description,
    url='https://github.com/scieloorg/opac_ssm_api',
    download_url='https://github.com/scieloorg/opac_ssm_api/tarball/' + __version__,
    license='BSD',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],
    keywords='',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='SciELO',
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='scielo@scielo.org',
    entry_points="""
    [console_scripts]
        generate_pb_files = opac_ssm_api.cli:main
    """)
