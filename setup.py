from setuptools import setup, find_packages


for line in open('drapery/__init__.py', 'r'):
    if line.find("__version__") >= 0:
        version = line.split("=")[1].strip()
        version = version.strip('"')
        version = version.strip("'")
        continue

with open('VERSION.txt', 'w') as fp:
    fp.write(version)

setup(name='drapery',
    version=version,
    author='Michael Rahnis',
    author_email='michael.rahnis@fandm.edu',
    description='Python library and CLI tool to convert 2D geometries to 3D given an elevation source',
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
    ]
)

