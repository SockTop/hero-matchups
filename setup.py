from setuptools import setup, find_packages

setup(name='hero-matrix',
      version='0.1',
      description='Dota2 drafting hero matchup helper',
      author='Sam Silberstein',
      packages=find_packages(),
      install_requires=[
        'beautifulsoup4==4.6.0',
        'click==6.7',
      ],
      entry_points={
          'console_scripts': [
              'matchups = hero_matrix:main'
          ]
      })
