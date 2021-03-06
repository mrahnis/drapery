from os import path
from setuptools import setup, find_packages


for line in open('drapery/__init__.py', 'r'):
    if line.find("__version__") >= 0:
        version = line.split("=")[1].strip()
        version = version.strip('"')
        version = version.strip("'")
        continue

with open('VERSION.txt', 'w') as fp:
    fp.write(version)

current_directory = path.abspath(path.dirname(__file__))
with open(path.join(current_directory, 'README.rst'), 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(name='drapery',
      version=version,
      author='Michael Rahnis',
      author_email='mike@topomatrix.com',
      description='Python library and CLI tool to convert 2D geometries to 3D given an elevation source',
      long_description=long_description,
      long_description_content_type='text/x-rst',
      url='http://github.com/mrahnis/drapery',
      license='BSD',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
          'rasterio',
          'fiona',
          'shapely',
          'click'
      ],
      entry_points='''
          [console_scripts]
          drape=drapery.cli.drape:cli
      ''',
      keywords='survey, conversion',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Topic :: Scientific/Engineering :: GIS'
      ])
