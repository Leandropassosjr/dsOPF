from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(name='opfython',
      version='1.0.4',
      description='Python-Inspired Optimum-Path Forest Classifier',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Gustavo Rosa',
      author_email='gth.rosa@uol.com.br',
      url='https://github.com/gugarosa/opfython',
      license='GPL-3.0',
      install_requires=['coverage>=4.5.2',
                        'numpy>=1.13.3',
                        'pylint>=1.7.4',
                        'pytest>=3.2.3'
                       ],
      extras_require={
          'tests': ['coverage',
                    'pytest',
                    'pytest-pep8',
                   ],
      },
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      packages=find_packages())
