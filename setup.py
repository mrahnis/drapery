from setuptools import setup, find_packages
import versioneer


with open('README.rst', 'r', encoding='utf-8') as f:
    long_description = f.read()
with open("requirements.txt", "r") as f:
    requirements = [line.strip() for line in f]

setup(name='drapery',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      author='Michael Rahnis',
      author_email='mike@topomatrix.com',
      description='Python library and CLI tool to convert 2D geometries to 3D given an elevation source',
      long_description=long_description,
      long_description_content_type='text/x-rst',
      url='http://github.com/mrahnis/drapery',
      license='BSD',
      packages=find_packages(),
      include_package_data=True,
      install_requires=requirements,
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
