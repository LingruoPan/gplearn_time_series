# 推荐你这样改：

from setuptools import setup, find_packages

DESCRIPTION = __doc__
VERSION = '0.5.dev0'

setup(name='gplearn_time_series',
      version=VERSION,
      description=DESCRIPTION,
      long_description=open("README.rst").read(),
      classifiers=['Development Status :: 3 - Alpha',
             'Intended Audience :: Science/Research',
             'Intended Audience :: Developers',
             'License :: OSI Approved',
             'Topic :: Software Development',
             'Topic :: Scientific/Engineering',
             'Operating System :: Microsoft :: Windows',
             'Operating System :: Unix',
             'Operating System :: MacOS',
             'Programming Language :: Python',
             'Programming Language :: Python :: 3',
             'Programming Language :: Python :: 3.8',
             'Programming Language :: Python :: 3.9',
             'Programming Language :: Python :: 3.10']
,
      author='Trevor Stephens',
      author_email='trev.stephens@gmail.com',
      url='https://github.com/LingruoPan/gplearn_time_series',
      license='new BSD',
      packages=find_packages(include=['gplearn_time_series', 'gplearn_time_series.*']),
      zip_safe=False,
      package_data={'': ['LICENSE']},
      install_requires=['scikit-learn>=1.0.2', 'joblib>=1.0.0'])
